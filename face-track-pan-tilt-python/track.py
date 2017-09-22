import io
import picamera
import cv2
import numpy
import time
import sys
from nanpy import (ArduinoApi, SerialManager, Servo)

SERVO_X_ARDUINO_PIN = 8
SERVO_Y_ARDUINO_PIN = 9
SERVO_ANGLE_STEP = 3 # deg

try:
  ArduinoApi(connection=SerialManager())
  servo_x = Servo(SERVO_X_ARDUINO_PIN)
  servo_y = Servo(SERVO_Y_ARDUINO_PIN)

except:
  print("Can't connect to arduino")
  sys.exit(0)

def create_video_stream():
  # Create a memory stream for video
  v_stream = io.BytesIO()
  # Setup camera options
  camera = picamera.PiCamera()
  camera.resolution = (320, 240)
  camera.framerate = 30
  camera.start_preview()
  camera.rotation = 180 # flip picture as camera is mounted upside-down
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
  if area > p_area:
    return current_face
  else:
    return previous_face

def get_biggest_face(faces):
  face_with_areas = map(extract_area_size, faces)
  biggest_face_with_area = reduce(keep_biggest, face_with_areas)
  _, biggest_face = biggest_face_with_area
  return biggest_face

def get_compensation_directions(face):

  x, y, w, h = biggest_face

  face_center_x = x + w / 2
  face_center_y = y + h / 2

  x0, y0 = camera_center
  center_rad = 10

  direction_x = "Center"
  direction_y = "Center"

  if face_center_x > (x0 + center_rad) :
    direction_x = "RIGHT"
  elif face_center_x < (x0 - center_rad) :
    direction_x = "LEFT"

  if face_center_y > (y0 + center_rad) :
    direction_y = "BOTTOM"
  elif face_center_y < (y0 - center_rad) :
    direction_y = "TOP"

  return (direction_x, direction_y)


camera = create_video_stream()
camera_center = map(lambda x: x/2, camera.resolution) # from camera resolution

# Face detection Haar cascade file
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

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
      # Look for the biggest face
      biggest_face = get_biggest_face(faces)

      # Compute compensation
      dx, dy = get_compensation_directions(biggest_face)

      if dx == "RIGHT":
        angle_x = angle_x - SERVO_ANGLE_STEP
      elif dx == "LEFT":
        angle_x = angle_x + SERVO_ANGLE_STEP

      if dy == "BOTTOM":
        angle_y = angle_y + SERVO_ANGLE_STEP
      elif dy == "TOP":
        angle_y = angle_y - SERVO_ANGLE_STEP

      servo_x.write(angle_x)
      servo_y.write(angle_y)

  except Exception as e:
    print e
    camera.stop_recording()
    sys.exit(0)
