from sense_hat import SenseHat
import math

sense = SenseHat()
sense.set_rotation(90)

colored = (218,112,214)
black = (0, 0, 0)

# Shift-lefting orientation angle
def shiftAngle (angle):
  return (angle - 180) if angle > 180 else (angle + 180)

def pixelRow(angle):
  normalized_angle = math.floor( 8 * shiftAngle(angle) / 360 )
  return [colored if i == normalized_angle else black for i in range(8)]

while True:
    roll = sense.get_orientation_degrees()['roll']

    pixels = []
    for num in range(8): pixels = pixels + pixelRow(roll)

    sense.set_pixels(pixels)
