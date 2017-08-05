from smbus import SMBus
import time

bus = SMBus(1) #Pi 3 uses device interface 1

DEVICE = 0x20 # Device address (A0-A2 all on ground)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs - not used here

# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE, IODIRA, 0x00) # 0 written here in hex

# bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, NUMBER)
bus.write_byte_data(DEVICE, OLATA, 0b111) # here 111 in binary so 7 in base 10
time.sleep(1)

# Set output all 7 output bits to 0
bus.write_byte_data(DEVICE, OLATA, 0)

for MyData in range(1, 8):
  # Count from 1 to 8 which in binary so 001 to 111
  bus.write_byte_data(DEVICE, OLATA, MyData)
  print(MyData, "in binary:", "{0:b}".format(MyData))
  time.sleep(3)

# Set all bits to zero
bus.write_byte_data(DEVICE, OLATA, 0)
