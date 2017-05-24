import RPi.GPIO as GPIO
import time
import atexit

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red_pin = 18
delay = 0.5

GPIO.setup(red_pin, GPIO.OUT)

def exit_handler():
    print("Cleaning up")
    GPIO.cleanup()

try:
    while True:
        GPIO.output(red_pin, True)
        time.sleep(delay)
        GPIO.output(red_pin, False)
        time.sleep(delay)
finally:
    exit_handler()

atexit.register(exit_handler)
