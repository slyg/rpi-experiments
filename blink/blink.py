import RPi.GPIO as GPIO
import time
import atexit

red_pin = 18
delay = 0.5

GPIO.setmode(GPIO.BCM)
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
