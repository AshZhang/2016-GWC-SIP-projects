from turtle import *

penup()
pendown()

def make_square(color):
	fillcolor(color)
	pencolor(color)
	begin_fill()
	for i in range (4):
		forward(50)
		right(90)
	end_fill()
	penup()
	forward(60)
	pendown()
	print(color)
	
shape("turtle")
color("tomato")

penup()
stamp()
for i in range(12):
	
	
done()