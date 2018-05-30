#importiamo le librerie per il controllo dell'interfaccia GPIO
import RPi.GPIO as GPIO
import time

#definiamo il sistema di riferimento dei pin. Con GPIO.BCM usiamo i numeri GPIO dei pin e non il numero dei pin. 
#Ad esempio con GPIO.BCM per riferirci al pin GPIO17, usiamo 17 (e non 11). Per indicare che 
#ci si riferisce al numero del pin, si usa GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

#definiamo il numero GPIO dei pin in gioco

pin8 = 17
pin9 = 18
pin10 = 19
pin11 = 20
pin12 = 21
pin13 = 22
pin14 = 23
pin15 = 24

pin0 = 9
pin1 = 10
pin2 = 11
pin3 = 12
pin4 = 13
pin5 = 14
pin6 = 15
pin7 = 16

pin16 = 4
pin17 = 5
pin18 = 6
pin19 = 7
pin20 = 8
pin21 = 25
pin22 = 26
pin23 = 27

pins = [pin0,
pin1,
pin2,
pin3 ,
pin4,
pin5,
pin6,
pin7,
pin8 ,
pin9 ,
pin10 ,
pin11 ,
pin12 ,
pin13,
pin14 ,
pin15 ,
pin16 ,
pin17 ,
pin18 ,
pin19 ,
pin20 ,
pin21,
pin22,
pin23]


#definiamo che pinLedLeft e pinLedRight sono due pin di output

class port_control():
	
	floor_lights_on = 		False
	heating_on = 			False
	signs_on = 				False
	ventialtion_fan_on = 	False
	trunk_lights_on = 		False
	driver_seat_light_on = 	False
	stop_request_light_on = False
	
	def init(self):				
		for pin_number in pins:
			GPIO.setup(pin_number , GPIO.OUT)
			GPIO.output(pin_number, GPIO.HIGH)

	def release(self):
		GPIO.cleanup()

	def set_off(self):
		print ("Shutting off")
		GPIO.output(pins[0], GPIO.HIGH)
		GPIO.output(pins[1], GPIO.HIGH)
		GPIO.output(pins[2], GPIO.HIGH)
		GPIO.output(pins[3], GPIO.HIGH)

	def set_1(self):
		print ("1")
		GPIO.output(pins[0], GPIO.LOW)
		GPIO.output(pins[1], GPIO.LOW)
		GPIO.output(pins[2], GPIO.HIGH)
		GPIO.output(pins[3], GPIO.HIGH)

	def set_2(self):
		print ("2")
		GPIO.output(pins[0], GPIO.LOW)
		GPIO.output(pins[1], GPIO.HIGH)
		GPIO.output(pins[2], GPIO.LOW)
		GPIO.output(pins[3], GPIO.HIGH)

	def set_3(self):
		print ("3")
		GPIO.output(pins[0], GPIO.LOW)
		GPIO.output(pins[1], GPIO.HIGH)
		GPIO.output(pins[2], GPIO.HIGH)
		GPIO.output(pins[3], GPIO.LOW)
		
	def lights_out(self):	#Guerrilla Radio!
		print ("lights out")
		GPIO.output(pins[4], GPIO.HIGH)	
		GPIO.output(pins[5], GPIO.HIGH)

	def lights_cold(self):
		print ("lights cold")
		GPIO.output(pins[4], GPIO.LOW)
		GPIO.output(pins[5], GPIO.HIGH)
		
	def lights_hot(self):
		print ("lights hot")
		GPIO.output(pins[4], GPIO.HIGH)
		GPIO.output(pins[5], GPIO.LOW)
		
	def door_switch(self):
		print "Door switch"
		#GPIO.output(pins[6, GPIO.HIGH)
		#time.sleep(0.5)
		GPIO.output(pins[6], GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(pins[6], GPIO.HIGH)

	def defrost(self):
		print "Sbrinamento"
		GPIO.output(pins[7], GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(pins[7], GPIO.HIGH)

		
	def floor_lights(self):
		if self.floor_lights_on == False:
			GPIO.output(pins[8], GPIO.LOW)
			self.floor_lights_on = True
			print "luci a pavimento ON"
		else:
			GPIO.output(pins[8], GPIO.HIGH)
			self.floor_lights = False
			print "luci a pavimento OFF"			

	def tendina_sx(self, stop = True, direction_up = True):
		if stop == True:
			print "tendina sx stop"
			GPIO.output(pins[8], GPIO.HIGH)
			GPIO.output(pins[9], GPIO.HIGH)
			return
			
		if direction_up == True:
			GPIO.output(pins[8], GPIO.LOW)
			GPIO.output(pins[9], GPIO.HIGH)		
			print "Tendina sx su"
		else:
			GPIO.output(pins[8], GPIO.HIGH)
			GPIO.output(pins[9], GPIO.LOW)
			print "Tendina sx giu,"

	def tendina_dx(self, stop = True, direction_up = True):
		if stop == True:
			GPIO.output(pins[10], GPIO.HIGH)
			GPIO.output(pins[11], GPIO.HIGH)
			print "tendina dx stop"
			return
		
		if direction_up == True:
			GPIO.output(pins[10], GPIO.LOW)
			GPIO.output(pins[11], GPIO.HIGH)
			print "Tendina dx su"
		else:
			GPIO.output(pins[10], GPIO.HIGH)
			GPIO.output(pins[11], GPIO.LOW)
			print "Tendina dx giu'"
		
	def heating(self):
		if self.heating_on == False:
			print "riscalndamento ON"
			GPIO.output(pins[14], GPIO.LOW)
			self.heating_on = True
		else:
			print "riscalndamento OFF"
			GPIO.output(pins[14], GPIO.HIGH)
			self.heating_on = False
			
		
	def front_door_switch(self):
		print "Front Door switch"
		GPIO.output(pins[15], GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(pins[15], GPIO.HIGH)
		
	def switch_signs(self):
		if self.signs_on == False:
			print "Cartelli ON"
			GPIO.output(pins[16], GPIO.LOW)
			self.signs_on = True
		else:
			print "cartelli OFF"
			GPIO.output(pins[16], GPIO.HIGH)
			self.signs_on = False
	
	def trunck_lights(self):
		if self.trunk_lights_on == False:
			print "Luce Bagagliaio ON"
			GPIO.output(pins[17], GPIO.LOW)
			self.trunk_lights_on = True
		else:
			print "Luce Bagagliaio OFF"
			GPIO.output(pins[17], GPIO.HIGH)
			self.trunk_lights_on = False
	
	def driver_seat_light(self):
		if self.driver_seat_light_on == False:
			print "Luce Autista ON"
			GPIO.output(pins[18], GPIO.LOW)
			self.driver_seat_light_on = True
		else:
			print "Luce Autista OFF"
			GPIO.output(pins[18], GPIO.HIGH)
			self.driver_seat_light_on = False
		
	
	def stop_request_light(self):
		if self.stop_request_light_on == False:
			print "Fermata Prenota ON"
			GPIO.output(pins[19], GPIO.LOW)
			self.stop_request_light_on = True
		else:
			print "Fermata Prenota OFF"
			GPIO.output(pins[19], GPIO.HIGH)
			self.stop_request_light_on = False

	
	def ventilation(self, status):
		
		if status > 0:
			GPIO.output(pins[13], GPIO.HIGH)
			GPIO.output(pins[13], GPIO.HIGH)
			self.ventialtion_fan_on = True
			print "Aspirazione"
		
		if status == 0:
			self.ventialtion_fan_on = False			
			GPIO.output(pins[12], GPIO.LOW)
			GPIO.output(pins[13], GPIO.HIGH)
			print "Aspirazione OFF"
			
		if status < 0:
			self.ventialtion_fan_on = True
			GPIO.output(pins[12], GPIO.HIGH)
			GPIO.output(pins[13], GPIO.LOW)
			print "Soffiaggio" 

'''	
def mini-bar-fridge():
	print "Frigorifero"
'''
