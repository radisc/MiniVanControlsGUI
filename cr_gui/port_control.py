#importiamo le librerie per il controllo dell'interfaccia GPIO
import RPi.GPIO as GPIO
import time

#definiamo il sistema di riferimento dei pin. Con GPIO.BCM usiamo i numeri GPIO dei pin e non il numero dei pin. 
#Ad esempio con GPIO.BCM per riferirci al pin GPIO17, usiamo 17 (e non 11). Per indicare che 
#ci si riferisce al numero del pin, si usa GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

#definiamo il numero GPIO dei pin in gioco
'''
pin0 = 17
pin1 = 18
pin2 = 19
pin3 = 20
pin4 = 21
pin5 = 22
pin6 = 23
pin7 = 24
'''
pin0 = 9
pin1 = 10
pin2 = 11
pin3 = 12
pin4 = 13
pin5 = 14
pin6 = 15
pin7 = 16


#definiamo che pinLedLeft e pinLedRight sono due pin di output
GPIO.setup(pin0 , GPIO.OUT)
GPIO.setup(pin1 , GPIO.OUT)
GPIO.setup(pin2 , GPIO.OUT)
GPIO.setup(pin3 , GPIO.OUT)
GPIO.setup(pin4 , GPIO.OUT)
GPIO.setup(pin5 , GPIO.OUT)
GPIO.setup(pin6 , GPIO.OUT)
GPIO.setup(pin7 , GPIO.OUT)

def init():
	GPIO.output(pin0, GPIO.HIGH)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)
	GPIO.output(pin4, GPIO.HIGH)
	GPIO.output(pin5, GPIO.HIGH)
	GPIO.output(pin6, GPIO.HIGH)
	GPIO.output(pin7, GPIO.HIGH)

def set_off():
	print ("Shutting off")
	GPIO.output(pin0, GPIO.HIGH)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)

def set_1():
	print ("1")
	GPIO.output(pin0, GPIO.LOW)
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.HIGH)

def set_2():
	print ("2")
	GPIO.output(pin0, GPIO.LOW)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.HIGH)

def set_3():
	print ("3")
	GPIO.output(pin0, GPIO.LOW)
	GPIO.output(pin1, GPIO.HIGH)
	GPIO.output(pin2, GPIO.HIGH)
	GPIO.output(pin3, GPIO.LOW)
	
def lights_out():	#Guerrilla Radio!
	print ("lights out")
	GPIO.output(pin4, GPIO.HIGH)	
	GPIO.output(pin5, GPIO.HIGH)

def lights_cold():
	print ("lights cold")
	GPIO.output(pin4, GPIO.LOW)
	GPIO.output(pin5, GPIO.HIGH)
	
def lights_hot():
	print ("lights hot")
	GPIO.output(pin4, GPIO.HIGH)
	GPIO.output(pin5, GPIO.LOW)
	
def door_switch():
	print "Door switch"
	#GPIO.output(pin6, GPIO.HIGH)
	#time.sleep(0.5)
	GPIO.output(pin6, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(pin6, GPIO.HIGH)


