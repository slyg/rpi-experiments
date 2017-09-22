from nanpy import (ArduinoApi, SerialManager, Servo)
from time import sleep
import sys

try:
  connection = SerialManager()
  a = ArduinoApi(connection=connection)
  a.pinMode(13, a.OUTPUT)
  servo = Servo(9)

except:
  print("Can't connect to arduino")
  sys.exit(0)

try:
  while True:
    a.digitalWrite(13, a.HIGH)
    servo.write(90)
    sleep(0.1)
    a.digitalWrite(13, a.LOW)
    servo.write(80)
    sleep(0.1)

except Exception:
  a.digitalWrite(13, a.LOW)
  servo.write(90)
  sys.exit(0)
