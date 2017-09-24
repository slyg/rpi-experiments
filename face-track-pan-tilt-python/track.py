import io
import picamera
import cv2
import numpy
import time
import sys
from nanpy import (ArduinoApi, SerialManager, Servo)
import RPi.GPIO as GPIO

### Setup of GPIO pin ###

FACE_DETECTION_STATUS_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(FACE_DETECTION_STATUS_PIN, GPIO.OUT)



### Setup of servo controls via arduino board ###

SERVO_X_ARDUINO_PIN = 8
SERVO_Y_ARDUINO_PIN = 9

try:
  connection = SerialManager()
  ArduinoApi(connection=connection)
  servo_x = Servo(SERVO_X_ARDUINO_PIN)
  servo_y = Servo(SERVO_Y_ARDUINO_PIN)

except Exception as e:
  print e
  sys.exit(0)



def create_video_stream():
  camera = picamera.PiCamera()
  camera.resolution = (320, 240)
  camera.framerate = 20
  camera.rotation = 180 # flip picture as camera is mounted upside-down

  v_stream = picamera.PiCameraCircularIO(camera, size=17000000)
  camera.start_recording(v_stream, format='h264', quality=30) # [0:high , 40:low]
  time.sleep(2) # warmup
  return camera

def extract_area_size(face):
  x, y, w, h = face
  area = w * h
  return (area, face)

def keep_biggest(previous_face, current_face):
  area, face = current_face
  p_area, p_face = previous_face
  return current_face if (area > p_area) else previous_face

def get_biggest_face(faces):
  face_with_areas = map(extract_area_size, faces)
  biggest_face_with_area = reduce(keep_biggest, face_with_areas)
  _, biggest_face = biggest_face_with_area
  return biggest_face

def get_compensation_angle(face):

  x, y, w, h = face

  # Position of the face
  face_x = x + w / 2
  face_y = y + h / 2

  # Camera parameters and mappings
  x0, y0 = camera_center
  x_op = float(50/2) # half opening of the cam in deg
  y_op = float(40/2) # half opening of the cam in deg
  cam_width = 320 # px
  cam_heigh = 240 # px

  # face position ratio
  face_ratio_x = float(face_x) / cam_width
  face_ratio_y = float(face_y) / cam_heigh

  # ratio to angle
  face_x_angle = int(x_op * (face_ratio_x - 0.5)) # deg
  face_y_angle = int(y_op * (face_ratio_y - 0.5)) # deg

  # Compute angle compensation
  compensation_angle_x = 0
  compensation_angle_y = 0

  if (face_x > x0) or (face_x < x0):
    compensation_angle_x = -1 * face_x_angle

  if (face_y > y0) or (face_y < y0) :
    compensation_angle_y = face_y_angle

  return (compensation_angle_x, compensation_angle_y)



### Setup of camera and pan-tilt ###

camera = create_video_stream()
camera_center = map(lambda x: x/2, camera.resolution) # from camera resolution

# Face detection Haar cascade file
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

# Initial pan-tilt angles
angle_x = 90
angle_y = 90
servo_x.write(angle_x)
servo_y.write(angle_y)

while True:

  try:

    # Create a memory stream to avoid photos needing to be saved in a file
    p_stream = io.BytesIO()
    camera.capture(p_stream, format='jpeg', use_video_port=True, thumbnail=None)

    buff = numpy.fromstring(p_stream.getvalue(), dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Look for faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.5, 2)

    if faces is not ():
      # Display face detection on a led
      GPIO.output(FACE_DETECTION_STATUS_PIN, True)

      # Look for the biggest face
      biggest_face = get_biggest_face(faces)

      # Compute pan-tilt angle to adjust centring
      ax, ay = get_compensation_angle(biggest_face)

      # Update angles values
      angle_x = angle_x + ax
      angle_y = angle_y + ay
      servo_x.write(angle_x)
      servo_y.write(angle_y)

    else:
      GPIO.output(FACE_DETECTION_STATUS_PIN, False)

  except Exception as e:
    print e
    camera.stop_recording()
    GPIO.output(FACE_DETECTION_STATUS_PIN, False)
    GPIO.cleanup()
    connection.flush_input()
    connection.close()
    sys.exit(0)
