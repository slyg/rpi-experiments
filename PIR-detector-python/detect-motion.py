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

PIR_PIN_MUM = 25

GPIO.setmode(GPIO.BCM) # Board BCM GPIO numbering
GPIO.setup(PIR_PIN_MUM, GPIO.IN) # Set pin 25 as input

# Main loop

delay = 1 # seconds

try:
  while True:
    if GPIO.input(PIR_PIN_MUM):
      print("Movement start")
    else:
      print("Movement stop")

    time.sleep(delay)

except: GPIO.cleanup()
finally: GPIO.cleanup()
