#Name:  Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu
#Date: 01-26-2021
# pink bg -- black triangle -- lightgreen pentagram 

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("cyan")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("red")
tess.pensize(5)

alex = turtle.Turtle()           # create alex

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(72)
tess.forward(80)
tess.left(72)
tess.forward(80)
tess.left(72)  # complete the triangle
tess.forward(80)
tess.left(72)
tess.forward(80)
tess.left(72)

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a square
alex.left(120)
alex.forward(50)
alex.left(120)
alex.forward(50)
alex.left(120)


