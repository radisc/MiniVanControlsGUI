#!/usr/bin/env python


import cv2
import numpy as np
import port_control

SIZE = 133

path = "/home/pi/MiniVanControlsGUI/cr_gui/icons/"

tile_list = [	"off.jpeg", 		"low.jpeg", 			"on.jpeg", 				"hi.jpeg",			"doors.jpeg", 
				"light-bulb-off.png","light-bulb-on-y.png", "light-bulb-on-b.png",	"tendina_sx.jpg", 	"tendina_dx.jpg",
				"riscaldamento.jpg", "porta_ant.jpg", 		"cartelli.jpg",			"lunotto_porta.jpg","luce_baga.jpg",	
				"luce_autista.jpg", "fermata_prenotata.jpg","aspiratore.jpg"]
image_list = []

blank = cv2.imread(path + "blank.jpg", 1)
blank = cv2.resize( blank, ( SIZE, SIZE) )	

global port_control
#Create

print ("Hello")

def callback(event,x,y,flags,param):
	
	if event == cv2.EVENT_LBUTTONDOWN:
		
		X = int(x / (SIZE)) + 1
		Y = int(y / (SIZE)) + 1
		
		X_x = x % SIZE
		Y_y = y % SIZE
		
		if X == 1 and Y == 1:
			port_control.set_off()

		if X == 2 and Y == 1:
			port_control.set_1()

		if X == 3 and Y == 1:
			port_control.set_2()

		if X == 4 and Y == 1:
			port_control.set_3()

		if X == 5 and Y == 1:
			port_control.door_switch()

		if X == 6 and Y == 1:
			port_control.lights_out()
			
		if X == 1 and Y == 2:
			port_control.lights_cold()

		if X == 2 and Y == 2:
			port_control.lights_hot()
			
		if X == 3 and Y == 2:
			
			if Y_y < SIZE / 3:
				port_control.tendina_sx(False, True)

			if SIZE / 3 < Y_y and Y_y < 2*SIZE/3:
				port_control.tendina_sx(True, True)
			
			if 2*SIZE/3 < Y_y:
				port_control.tendina_sx(False, False)
		
		if X == 4 and Y == 2:
			if Y_y < SIZE / 3:
				port_control.tendina_dx(False, True)

			if SIZE / 3 < Y_y and Y_y < 2*SIZE/3:
				port_control.tendina_dx(True, True)
			
			if 2*SIZE/3 < Y_y:
				port_control.tendina_dx(False, False)
					
		if X == 5 and Y == 2:
			port_control.heating()
		
		if X == 6 and Y == 2:
			port_control.front_door_switch()	
					
		if X == 1 and Y == 3:
			port_control.switch_signs()
						
		if X == 2 and Y == 3:			
			port_control.defrost()
		
		if X == 3 and Y == 3:			
			port_control.trunck_lights()
	
		if X == 4 and Y == 3:
			port_control.driver_seat_light()
		
		if X == 5 and Y == 3:
			port_control.stop_request_light()
		
		if X == 6 and Y == 3:
			if Y_y < SIZE / 3:
				port_control.ventilation(1)

			if SIZE / 3 < Y_y and Y_y < 2*SIZE/3:
				port_control.ventilation(0)
			
			if 2*SIZE/3 < Y_y:
				port_control.ventilation(-1)
		
							
def draw_canvas(image_list):
	
	for name in tile_list:
		image_list.append(cv2.resize(cv2.imread(path + name, 1), ( SIZE, SIZE) ))	
	
	image_list.append(blank)
	image_list.append(blank)
	image_list.append(blank)
	image_list.append(blank)
	image_list.append(blank)
	image_list.append(blank)
	image_list.append(blank)

	
	
	canvas = np.vstack( ( 	
							np.hstack(	(image_list[0], 	image_list[1],	image_list[2],	image_list[3],		image_list[4], 	image_list[5]   ) 	),
							np.hstack(	(image_list[6],		image_list[7],	image_list[8],	image_list[9], 		image_list[10],	image_list[11]	)   ),
							np.hstack(	(image_list[12],	image_list[13],	image_list[14], image_list[15], 	image_list[16],	image_list[17]  ) 	)
							#,np.hstack(	(image_list[18],	image_list[19], image_list[20], image_list[21], 	image_list[22],	image_list[23])	) 
							) )
	
	return canvas


if __name__ == "__main__":
	
	canvas = draw_canvas(image_list)
		
	cv2.namedWindow('main', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('main', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
	cv2.setMouseCallback('main',callback)
	cv2.imshow('main', canvas)
	cv2.waitKey(1)
	
	port_control = port_control.port_control()
	port_control.init()
	
	while(1):
		cv2.imshow('main', canvas)
		if cv2.waitKey(40) & 0xFF == 27:
			break
	cv2.destroyAllWindows()
	port_control.release()
