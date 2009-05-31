from turtle import *
import serial

ser = serial.Serial('/dev/tty.usbserial-A60049lS', 115200)

goto(0,0)
clear()
speed('fast')

fwd = lft = bck = rht = 0 
	
while 1:
	lect = ser.read()
	
	
	if lect == 'a':
		up() 
	if lect == 'b':
		down() 
	if lect == 'l':
		lft = 10  
	if lect == 'r':
		rht = 10 
	if lect == 'u':
		fwd = 10 
	if lect == 'd':
		bck = 10 
	if lect == 's':
		goto(0,0)
		
	forward(fwd)
	left(lft)
	backward(bck)
	right(rht)