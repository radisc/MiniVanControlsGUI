#!/usr/bin/env python

import MCP230xx

import cv2
import numpy as np
import port_control

global path
global SIZE

SIZE = 200
port_control.init()

# mouse callback function
def ac_cb(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		if x < int(SIZE/2.) and y < int(SIZE/2.):
			port_control.set_off()

		if x > int(SIZE/2.) and y < int(SIZE/2.):
			port_control.set_1()

		if x < int(SIZE/2.) and y > int(SIZE/2.):
			port_control.set_2()

		if x > int(SIZE/2.) and y > int(SIZE/2.):
			port_control.set_3()
			
def lights_cb(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		if SIZE < x and x < int(3*SIZE/4.) and y < int(SIZE/2.):
			port_control.lights_out()

		if x > int(3*SIZE/4.) and y < int(SIZE/2.):
			#port_control.lights_out()
			port_control.door_switch()
			
		if SIZE < x and x < int(3*SIZE/4.) and y > int(SIZE/2.):
			port_control.lights_cold()

		if x > int(3*SIZE/4.) and y > int(SIZE/2.):
			port_control.lights_hot()

def callback(event,x,y,flags,param):
	
	if event == cv2.EVENT_LBUTTONDOWN:
		
		X = int(x / (SIZE/2)) + 1
		Y = int(y / (SIZE/2)) + 1
		
		if X == 1 and Y == 1:
			port_control.set_off()

		if X == 2 and Y == 1:
			port_control.set_1()

		if X == 1 and Y == 2:
			port_control.set_2()

		if X == 2 and Y == 2:
			port_control.set_3()

		if X == 3 and Y == 1:
			port_control.lights_out()

		if X == 4 and Y == 1:
			#port_control.lights_out()
			port_control.door_switch()
			
		if X == 3 and Y == 2:
			port_control.lights_cold()

		if X == 4 and Y == 2:
			port_control.lights_hot()


def create_buttoned_window(imgs_list , window_name , callback):
	
	img = np.ones((SIZE,SIZE,3), np.uint8)
	img.fill(255)
	cv2.line(img, (int(SIZE/2.), 0), (int(SIZE/2.),SIZE), (0,0,0))
	cv2.line(img, (0, int(SIZE/2.)), (SIZE, int(SIZE/2.)), (0,0,0))
	cv2.namedWindow(window_name)
	cv2.moveWindow(window_name, SIZE,20)
	cv2.setMouseCallback(window_name,callback)

	off_img = cv2.resize(cv2.imread(path + imgs_list[0], 1), ( SIZE/2, SIZE/2) )
	low_img = cv2.resize(cv2.imread(path + imgs_list[1], 1), ( SIZE/2, SIZE/2) )
	on_img  = cv2.resize(cv2.imread(path + imgs_list[2],  1), ( SIZE/2, SIZE/2) )
	hi_img  = cv2.resize(cv2.imread(path + imgs_list[3],  1), ( SIZE/2, SIZE/2) )

	top = np.hstack((off_img, low_img))
	bottom = np.hstack((on_img, hi_img))
	img = np.vstack((top, bottom)) 
	
	print ("creating window from paths")
	
	return img

# Create a black image, a window and bind the function to window
img = np.ones((SIZE,SIZE,3), np.uint8)
img.fill(255)
cv2.line(img, (int(SIZE/2.), 0), (int(SIZE/2.),SIZE), (0,0,0))
cv2.line(img, (0, int(SIZE/2.)), (SIZE, int(SIZE/2.)), (0,0,0))
cv2.namedWindow('main', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('main', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);

cv2.moveWindow("main", 0,20)
#cv2.setMouseCallback('main',ac_cb)

#load images
#cv2.imshow("s<dfasdf",image)

path = "/home/pi/MiniVanControlsGUI/cr_gui"

off_img = cv2.resize(cv2.imread(path + "/icons/off.jpeg", 1), ( SIZE/2, SIZE/2) )
low_img = cv2.resize(cv2.imread(path + "/icons/low.jpeg", 1), ( SIZE/2, SIZE/2) )
on_img  = cv2.resize(cv2.imread(path + "/icons/on.jpeg",  1), ( SIZE/2, SIZE/2) )
hi_img  = cv2.resize(cv2.imread(path + "/icons/hi.jpeg",  1), ( SIZE/2, SIZE/2) )

top = np.hstack((off_img, low_img))
bottom = np.hstack((on_img, hi_img))
img = np.vstack((top, bottom)) 

'''
#Create lights image
lights_image = np.ones((SIZE,SIZE,3), np.uint8)
lights_image.fill(255)
cv2.line(lights_image, (int(SIZE/2.), 0), (int(SIZE/2.),SIZE), (0,0,0))
cv2.line(lights_image, (0, int(SIZE/2.)), (SIZE, int(SIZE/2.)), (0,0,0))
cv2.namedWindow('lights_image')
cv2.moveWindow("lights_image", SIZE,20)
cv2.setMouseCallback('lights_image',lights_cb)

doors_img = cv2.resize(cv2.imread(path + "/icons/doors.jpeg", 1), ( SIZE/2, SIZE/2) )
lights_off_img = cv2.resize(cv2.imread(path + "/icons/light-bulb-off.jpeg", 1), ( SIZE/2, SIZE/2) )
lights_on_hot_img  = cv2.resize(cv2.imread(path + "/icons/light-bulb-on-y.jpeg",  1), ( SIZE/2, SIZE/2) )
lights_on_cold_img  = cv2.resize(cv2.imread(path + "/icons/light-bulb-on-b.jpeg",  1), ( SIZE/2, SIZE/2) )

top = np.hstack((lights_off_img, doors_img))
bottom = np.hstack((lights_on_cold_img, lights_on_hot_img))
lights_image = np.vstack((top, bottom)) 
'''

path_list = ["/icons/doors.jpeg", "/icons/light-bulb-off.png", "/icons/light-bulb-on-y.png", "/icons/light-bulb-on-b.png"]

lights_image = create_buttoned_window(path_list, "main", callback)

canvas = np.hstack((img, lights_image))

#mcp = MCP230xx.MCP23017(busnum = 1, address = 0x20)

#exit()

while(1):
    cv2.imshow('main',canvas)
    #cv2.imshow('lights_image', lights_image)
    if cv2.waitKey(40) & 0xFF == 27:
        break
cv2.destroyAllWindows()
