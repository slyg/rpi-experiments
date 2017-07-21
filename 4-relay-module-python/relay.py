import RPi.GPIO as GPIO
import time
import signal
import sys

# Exit handling

def exit_handler(signal, frame):
  GPIO.cleanup()
  sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

# GPIO and pins setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin_numbers = [12, 16, 20, 21]

for num in pin_numbers: GPIO.setup(num, GPIO.OUT)

# Main loop

delay = 1

while True:

  GPIO.output(pin_numbers[0], 1)
  time.sleep(delay/10)
  GPIO.output(pin_numbers[1], 1)
  time.sleep(delay/10)
  GPIO.output(pin_numbers[2], 1)
  time.sleep(delay/10)
  GPIO.output(pin_numbers[3], 1)
  time.sleep(delay/10)

  GPIO.output(pin_numbers[0], 0)
  time.sleep(delay/10)
  GPIO.output(pin_numbers[1], 0)
  time.sleep(delay/10)
  GPIO.output(pin_numbers[2], 0)
  time.sleep(delay/10)
  GPIO.output(pin_numbers[3], 0)
  time.sleep(delay/10)
