

#Name:  Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu
#Date: 01-26-2021
# Draws a hexagon

import turtle
wn = turtle.Screen()
thomasH = turtle.Turtle()
thomasH.color("#9BA17B")
thomasH.shape("turtle")


for i in range(6):
     thomasH.forward(150)
     thomasH.left(60)

wn.exitonclick()
