from sense_hat import SenseHat

sense = SenseHat()

colored = (218,112,214)
black = (0, 0, 0)

while True:
    rawOrientation = sense.get_orientation_degrees()['roll']

    # Shift-lefting orientation angle
    orientation = (rawOrientation - 180) if rawOrientation > 180 else (rawOrientation + 180)
    normalizedOrientation = 64 * orientation / 360

    pixels = [colored if i < normalizedOrientation else black for i in range(64)]

    sense.set_pixels(pixels)
