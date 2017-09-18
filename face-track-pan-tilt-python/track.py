import io
import picamera
import cv2
import numpy
import time
import sys
import RPi.GPIO as GPIO

SERVO_X_PIN = 32
SERVO_Y_PIN = 31
SERVO_ANGLE_STEP = 5 # deg

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_X_PIN, GPIO.OUT)
GPIO.setup(SERVO_Y_PIN, GPIO.OUT)
GPIO.setwarnings(False)

servo_frequency = 50 # 50Hz <=> 20ms cycle
servo_x = GPIO.PWM(SERVO_X_PIN, 50)
servo_y = GPIO.PWM(SERVO_Y_PIN, 50)

def create_video_stream():
  # Create a memory stream for video
  v_stream = io.BytesIO()
  # Setup camera options
  camera = picamera.PiCamera()
  camera.resolution = (320, 240)
  camera.start_preview()
  camera.rotation = 180 # flip picture as camera is mounted upside-down
  camera.start_recording(v_stream, format='h264', quality=20) # [0:high , 40:low]
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
  center_rad = 20

  direction_x = "Center"
  direction_y = "Center"

  if face_center_x > (x0 + center_rad) :
    direction_x = "Right"
  elif face_center_x < (x0 - center_rad) :
    direction_x = "Left"

  if face_center_y > (y0 + center_rad) :
    direction_y = "Bottom"
  elif face_center_y < (y0 - center_rad) :
    direction_y = "Top"

  return (direction_x, direction_y)

def angle_to_duty(angle):
  if angle > 179 :
    return angle_to_duty(179)
  elif angle < 1 :
    return angle_to_duty(1)
  else :
    return float(angle) / 18 + 2.5


camera = create_video_stream()
camera_center = map(lambda x: x/2, camera.resolution) # from camera resolution

# Face detection Haar cascade file
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

angle_x = 90
angle_y = 90

servo_x.start(angle_to_duty(angle_x))
servo_y.start(angle_to_duty(angle_y))

time.sleep(1)

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

      if dx == "Right":
        angle_x = angle_x - SERVO_ANGLE_STEP
      elif dx == "Left":
        angle_x = angle_x + SERVO_ANGLE_STEP

      if dy == "Bottom":
        angle_y = angle_y + SERVO_ANGLE_STEP
      elif dy == "Top":
        angle_y = angle_y - SERVO_ANGLE_STEP

      servo_x.ChangeDutyCycle(angle_to_duty(angle_x))
      servo_y.ChangeDutyCycle(angle_to_duty(angle_y))

      print "tick " + dx + ":" + dy

  except Exception as e:
    print e
    camera.stop_recording()
    GPIO.cleanup()
    sys.exit(0)
