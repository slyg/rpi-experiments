from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import random
import signal
import sys

# Exit handling

def exit_handler(signal, frame):
  sense.clear()
  sys.exit(0)

signal.signal(signal.SIGTERM, exit_handler)

# Sense hat setup

sense = SenseHat()

PIX_NUM = 64
COLOUR_MTX = [(52, 156, 163) for i in range(PIX_NUM)]
BLACK_MTX = [(0, 0, 0) for i in range(PIX_NUM)]

# MQTT setup

BROKER_ADDR = 'rpi-01'

def on_message(client, userdata, message):
  msg = str(message.payload.decode('utf-8'))
  print(msg)
  pixels = COLOUR_MTX if msg == 'ON' else BLACK_MTX
  sense.set_pixels(pixels)

mqttc = mqtt.Client()
mqttc.connect(BROKER_ADDR)
mqttc.subscribe('house/motion')
mqttc.on_message = on_message
mqttc.loop_forever()
