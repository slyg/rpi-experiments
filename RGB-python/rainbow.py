import RPi.GPIO as GPIO
import time
import signal
import sys
import random

# Exit handling

def exit_handler(signal, frame):
  GPIO.cleanup()
  sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

# GPIO and pins setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin_numbers = [18, 23, 24] # RGB

def power_mode_setup(pin_num):
  GPIO.setup(pin_num, GPIO.OUT)
  pin = GPIO.PWM(pin_num, 100)
  pin.start(0)
  return pin

pwm_pins = list(map(power_mode_setup, pin_numbers))

# Main loop

delay = 0.2

try:
  while True:
    for pin in pwm_pins: pin.ChangeDutyCycle(random.randint(0, 100))
    time.sleep(delay)

except: GPIO.cleanup()
finally: GPIO.cleanup()
