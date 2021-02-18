#Name:  Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu
#Date: 01-26-2021
# Draws a star flower

import turtle
wn = turtle.Screen()

wn.bgcolor('cyan')
tom = turtle.Turtle()
tom.pencolor('red')
tom.fillcolor('yellow')
tom.shape('turtle')

for i in range(18): 
    tom.forward(200)
    tom.left(140)
    tom.stamp()

    
wn.exitonclick()