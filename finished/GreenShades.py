#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import turtle				#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")		#Make it turtle shaped
tess.backward(300)			#Move her backwards, to give more space to draw



for i in range(0,255,10):
     
     tess.forward(10)		
     tess.pensize(i)		#Set the drawing size to be i (larger each time)
     tess.color(0,i,0)		#Set the red channel to be i (brighter each time)
     
tess.penup()
tess.forward(300)
tess.pendown()

for i in range(255,0,-10):
     tess.forward(10)
     tess.pensize(i)
     tess.color(0,i,0)
     

     
     
     
 