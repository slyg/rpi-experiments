import io
import picamera
import cv2
import numpy
import time
import sys

# Face detection Haar cascade file
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

# Create a memory stream for video
v_stream = io.BytesIO()

# Setup camera options
camera = picamera.PiCamera()

camera.resolution = (320, 240)
camera.color_effects = (128,128) # black and white capture
camera.start_preview()
camera.rotation = 180
camera.start_recording(v_stream, format='h264', quality=10) # 0:high / 40:low

camera_center = (160, 120) # from camera resolution

time.sleep(1)

def extract_area_size(face):
  x,y,w,h = face
  area = w * h
  return (area, face)

def keep_biggest(previous_face, current_face):
  area, face = current_face
  p_area, p_face = previous_face
  if area > p_area:
    return current_face
  else:
    return previous_face

while True:

  try:

    # Create a memory stream to avoid photos needing to be saved in a file
    p_stream = io.BytesIO()
    camera.capture(p_stream, format='jpeg', use_video_port=True, thumbnail=None)

    buff = numpy.fromstring(p_stream.getvalue(), dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Look for faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if faces is not ():
      face_with_areas = map(extract_area_size, faces)
      biggest_face = reduce(keep_biggest, face_with_areas)
      _, face = biggest_face
      x, y, w, h = face
      print "Face detected at " + str(x) + ":" + str(y)

  except:
    camera.stop_recording()
    sys.exit(0)
