import time
import smbus



pins = []

for i in range(22, 45):
	pins.append(i)


bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
HIGH = 1
LOW = 0


def i2c_out(pin_N, state):
	#try:
	bus.write_i2c_block_data(DEVICE_ADDRESS, pin_N, [state])
	#except(IOError) as e:
		#print("IOError: " + str(e))
	#	pass
	
	

class port_control():
	
	floor_lights_on = 		False
	heating_on = 			False
	signs_on = 				False
	ventialtion_fan_on = 	False
	trunk_lights_on = 		False
	driver_seat_light_on = 	False
	stop_request_light_on = False
	
	'''
	def init(self):				
		for pin_number in pins:
			GPIO.setup(pin_number , GPIO.OUT)
			i2c_out(pin_number, GPIO.HIGH)

	def release(self):
		GPIO.cleanup()
	'''
	
	def set_off(self):
		print ("Shutting off")
		i2c_out(pins[0], HIGH)
		i2c_out(pins[1], HIGH)
		i2c_out(pins[2], HIGH)
		time.sleep(0.1)
		i2c_out(pins[3], HIGH)

	def set_1(self):
		print ("1")
		i2c_out(pins[0], LOW)
		i2c_out(pins[1], LOW)
		i2c_out(pins[2], HIGH)
		time.sleep(0.1)
		i2c_out(pins[3], HIGH)

	def set_2(self):
		print ("2")
		i2c_out(pins[0], LOW)
		i2c_out(pins[1], HIGH)
		i2c_out(pins[2], LOW)
		time.sleep(0.1)
		i2c_out(pins[3], HIGH)

	def set_3(self):
		print ("3")
		i2c_out(pins[0], LOW)
		i2c_out(pins[1], HIGH)
		i2c_out(pins[2], HIGH)
		time.sleep(0.1)
		i2c_out(pins[3], LOW)
		
	def lights_out(self):	#Guerrilla Radio!
		print ("lights out")
		i2c_out(pins[4], HIGH)	
		i2c_out(pins[5], HIGH)

	def lights_cold(self):
		print ("lights cold")
		i2c_out(pins[4], LOW)
		i2c_out(pins[5], HIGH)
		
	def lights_hot(self):
		print ("lights hot")
		i2c_out(pins[4], HIGH)
		i2c_out(pins[5], LOW)
		
	def door_switch(self):
		print "Door switch"
		#i2c_out(pins[6, HIGH)
		#time.sleep(0.5)
		i2c_out(pins[6], LOW)
		time.sleep(0.5)
		i2c_out(pins[6], HIGH)

	def defrost(self):
		print "Sbrinamento"
		i2c_out(pins[7], LOW)
		time.sleep(0.5)
		i2c_out(pins[7], HIGH)

		
	def floor_lights(self):
		if self.floor_lights_on == False:
			i2c_out(pins[8], LOW)
			self.floor_lights_on = True
			print "luci a pavimento ON"
		else:
			i2c_out(pins[8], HIGH)
			self.floor_lights = False
			print "luci a pavimento OFF"			

	def tendina_sx(self, stop = True, direction_up = True):
		if stop == True:
			print "tendina sx stop"
			i2c_out(pins[8], HIGH)
			i2c_out(pins[9], HIGH)
			return
			
		if direction_up == True:
			i2c_out(pins[8], LOW)
			i2c_out(pins[9], HIGH)		
			print "Tendina sx su"
		else:
			i2c_out(pins[8], HIGH)
			i2c_out(pins[9], LOW)
			print "Tendina sx giu,"

	def tendina_dx(self, stop = True, direction_up = True):
		if stop == True:
			i2c_out(pins[10], HIGH)
			i2c_out(pins[11], HIGH)
			print "tendina dx stop"
			return
		
		if direction_up == True:
			i2c_out(pins[10], LOW)
			i2c_out(pins[11], HIGH)
			print "Tendina dx su"
		else:
			i2c_out(pins[10], HIGH)
			i2c_out(pins[11], LOW)
			print "Tendina dx giu'"
		
	def heating(self):
		if self.heating_on == False:
			print "riscalndamento ON"
			i2c_out(pins[14], LOW)
			self.heating_on = True
		else:
			print "riscalndamento OFF"
			i2c_out(pins[14], HIGH)
			self.heating_on = False
			
		
	def front_door_switch(self):
		print "Front Door switch"
		i2c_out(pins[15], LOW)
		time.sleep(0.5)
		i2c_out(pins[15], HIGH)
		
	def switch_signs(self):
		if self.signs_on == False:
			print "Cartelli ON"
			i2c_out(pins[16], LOW)
			self.signs_on = True
		else:
			print "cartelli OFF"
			i2c_out(pins[16], HIGH)
			self.signs_on = False
	
	def trunck_lights(self):
		if self.trunk_lights_on == False:
			print "Luce Bagagliaio ON"
			i2c_out(pins[17], LOW)
			self.trunk_lights_on = True
		else:
			print "Luce Bagagliaio OFF"
			i2c_out(pins[17], HIGH)
			self.trunk_lights_on = False
	
	def driver_seat_light(self):
		if self.driver_seat_light_on == False:
			print "Luce Autista ON"
			i2c_out(pins[18], LOW)
			self.driver_seat_light_on = True
		else:
			print "Luce Autista OFF"
			i2c_out(pins[18], HIGH)
			self.driver_seat_light_on = False
		
	
	def stop_request_light(self):
		if self.stop_request_light_on == False:
			print "Fermata Prenota ON"
			i2c_out(pins[19], LOW)
			self.stop_request_light_on = True
		else:
			print "Fermata Prenota OFF"
			i2c_out(pins[19], HIGH)
			self.stop_request_light_on = False

	
	def ventilation(self, status):
		
		if status > 0:
			i2c_out(pins[13], HIGH)
			i2c_out(pins[13], HIGH)
			self.ventialtion_fan_on = True
			print "Aspirazione"
		
		if status == 0:
			self.ventialtion_fan_on = False			
			i2c_out(pins[12], LOW)
			i2c_out(pins[13], HIGH)
			print "Aspirazione OFF"
			
		if status < 0:
			self.ventialtion_fan_on = True
			i2c_out(pins[12], HIGH)
			i2c_out(pins[13], LOW)
			print "Soffiaggio" 

'''	
def mini-bar-fridge():
	print "Frigorifero"
'''
