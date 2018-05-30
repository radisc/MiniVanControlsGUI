#!/usr/bin/env python

import socket
import time

UDP_IP = "192.168.1.177"
UDP_PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

i = 22
s = 0

while True:
	sock.sendto(str(i)+","+str(s), (UDP_IP,UDP_PORT))
	print "sent " + str(i)+","+str(s)
	time.sleep(0.1)
	i = i + 1
	if (i == 46):
		i = 22
		s = (1 - s)
