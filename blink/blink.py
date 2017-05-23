import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red_pin = 18
delay = 0.2

GPIO.setup(red_pin, GPIO.OUT)


try:
    while True:
        GPIO.output(red_pin, True)
        time.sleep(delay)
        GPIO.output(red_pin, False)
        time.sleep(delay)
finally:
    print("Cleaning up")
    GPIO.cleanup()
