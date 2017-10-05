import RPi.GPIO as GPIO
import time

def init():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17, GPIO.OUT)
  GPIO.setup(22, GPIO.OUT)
  GPIO.setup(23, GPIO.OUT)
  GPIO.setup(24, GPIO.OUT)

def backward(t):
  init()
  GPIO.output(17, False)
  GPIO.output(22, True)
  GPIO.output(23, False)
  GPIO.output(24, True)
  time.sleep(t)
  GPIO.cleanup()

def forward(t):
  init()
  GPIO.output(17, True)
  GPIO.output(22, False)
  GPIO.output(23, True)
  GPIO.output(24, False)
  time.sleep(t)
  GPIO.cleanup()

def left():
  init()
  GPIO.output(17, False)
  GPIO.output(22, True)
  GPIO.output(23, True)
  GPIO.output(24, False)
  time.sleep(0.4)
  GPIO.cleanup()

def right():
  init()
  GPIO.output(17, True)
  GPIO.output(22, False)
  GPIO.output(23, False)
  GPIO.output(24, True)
  time.sleep(0.4)
  GPIO.cleanup()

forward(1)
time.sleep(0.5)
left()
time.sleep(0.5)
forward(1)
time.sleep(0.5)
backward(1)
time.sleep(0.5)
right()
time.sleep(0.5)
backward(1)
