#Name:  Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import turtle
wn = turtle.Screen()

userColor = input('Enter Hex Code: ')
userColor = '#' + userColor




tom = turtle.Turtle()
tom.color(userColor)
tom.shape('turtle')

for i in range(5): 
    tom.stamp()
    tom.penup()
    tom.forward(50)
    tom.pendown()
    

    
wn.exitonclick()