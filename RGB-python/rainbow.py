import RPi.GPIO as GPIO
import time
import signal
import sys

red_pin = 18
delay = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)

def exit_handler(signal, frame):
  GPIO.cleanup()
  sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

try:
  while True:
    GPIO.output(red_pin, True)
    time.sleep(delay)
    GPIO.output(red_pin, False)
    time.sleep(delay)

except KeyboardInterrupt:
  GPIO.cleanup()

finally:
  GPIO.cleanup()
