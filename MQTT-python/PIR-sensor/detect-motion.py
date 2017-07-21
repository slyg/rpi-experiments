import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import signal
import sys

# Exit handling

def exit_handler():
  GPIO.cleanup()
  sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

# Establish MQTT connection

BROKER_ADDR = 'rpi-01'

client = mqtt.Client()      # create new instance
client.connect(BROKER_ADDR) # connect to broker

# GPIO and pins setup

PIR_PIN_NUM = 25
LED_PIN_NUM = 18

GPIO.setmode(GPIO.BCM) # Board BCM GPIO numbering
GPIO.setup(PIR_PIN_NUM, GPIO.IN) # Set pin 25 as input
GPIO.setup(LED_PIN_NUM, GPIO.OUT, initial = 0) # Set pin 18 as output

# Main loop

delay = 0.2 # seconds

while True:
  motion_detected = GPIO.input(PIR_PIN_NUM)
  GPIO.output(LED_PIN_NUM, 1 if motion_detected else 0)
  client.publish('house/motion', 'ON' if motion_detected else 'OFF')
  time.sleep(delay)
