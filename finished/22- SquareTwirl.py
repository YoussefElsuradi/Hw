#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import turtle

Tess = turtle.Turtle()
#Tess.speed(0)
side=25


for i in range (100):
    side=side*1.02
    Tess.right(5)
    for i in range(4):
        Tess.forward(side)
        Tess.right(90)
   


Tess.penup()


