#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import turtle
import random

trey = turtle.Turtle()
trey.speed(200)

for i in range(200):
    if i % 10 == 0 :
        trey.penup()
        trey.forward(20)
        trey.pendown()    
    else:
        
        trey.forward(10)
    a = random.randrange(0,360,45)
    trey.right(a)
