from turtle import *
goto(0,0)
clear()
speed('fast')
for step in range(500):
	forward(step)
	left(20)
	backward(step)
	right(10)
raw_input()