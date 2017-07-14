from sense_hat import SenseHat
import math

sense = SenseHat()
sense.set_rotation(90)

colours_per_row = [
  (242,6,104),
  (252,94,48),
  (250,149,23),
  (52,156,163),
  (52,156,163),
  (250,149,23),
  (252,94,48),
  (242,6,104)
]

black = (0, 0, 0)

# Shift-lefting orientation angle
def shiftAngle (angle):
  return (angle - 180) if angle > 180 else (angle + 180)

def pixelRow(angle):
  normalized_angle = math.floor( 8 * shiftAngle(angle) / 360 )
  return [colours_per_row[i] if i == normalized_angle else black for i in range(8)]

while True:
    roll = sense.get_orientation_degrees()['roll']

    pixels = []
    for num in range(8): pixels = pixels + pixelRow(roll)

    sense.set_pixels(pixels)
