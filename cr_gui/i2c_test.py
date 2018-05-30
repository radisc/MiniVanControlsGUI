import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
#Write an array of registers

i = 22
s = 0

while True:
	ledout_values = [i]
	#bus.write_byte(DEVICE_ADDRESS, i)
	try:
		bus.write_i2c_block_data(0x20, i, [s])
	except(IOError):
		print "i2c bus error"
		pass
	
	print "sent " +str(i)
	time.sleep(0.5)
	i = i + 1
	if (i == 46):
		i = 22
		s = (1 - s)
