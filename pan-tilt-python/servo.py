import RPi.GPIO as GPIO
import time
import sys

SERVO_HORIZONTAL_PIN = 32
SERVO_VERTICAL_PIN = 31
SERVO_ANGLE_DELAY = 0.005 # sec

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_HORIZONTAL_PIN, GPIO.OUT)
GPIO.setup(SERVO_VERTICAL_PIN, GPIO.OUT)
GPIO.setwarnings(False)

servo_horizontal = GPIO.PWM(SERVO_HORIZONTAL_PIN, 50)  # 50Hz <=> 20ms cycle
servo_vertical = GPIO.PWM(SERVO_VERTICAL_PIN, 50)  # 50Hz <=> 20ms cycle

def angle_to_duty(angle):
  return float(angle) / 18 + 2.5

servo_horizontal.start(angle_to_duty(90))
servo_vertical.start(angle_to_duty(90))

time.sleep(1)

def cycle_1(servo):
  for angle in range(90, 170):
      servo.ChangeDutyCycle(angle_to_duty(angle))
      time.sleep(SERVO_ANGLE_DELAY)

def cycle_2(servo):
  for angle in range(170, 30, -1):
      servo.ChangeDutyCycle(angle_to_duty(angle))
      time.sleep(SERVO_ANGLE_DELAY)

def cycle_3(servo):
  for angle in range(30, 90):
      servo.ChangeDutyCycle(angle_to_duty(angle))
      time.sleep(SERVO_ANGLE_DELAY)

while True:
  try:
    cycle_1(servo_horizontal)
    cycle_1(servo_vertical)
    cycle_2(servo_horizontal)
    cycle_2(servo_vertical)
    cycle_3(servo_horizontal)
    cycle_3(servo_vertical)

  except:
    servo_horizontal.stop()
    GPIO.cleanup()
    sys.exit(0)
