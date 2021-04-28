#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu


import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
tess.shape('turtle')
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'r':          #turn red
        tess.color("red")
    elif ch == 'g':          #turn green
        tess.color("green")
    elif ch == 'b':          #turn blue
        tess.color("blue")
    elif ch == 'c':          #turn cyan
        tess.color("cyan")
    elif ch == 'T':        
        tess.stamp()
    elif ch == 'F':          
        tess.forward(50)
    elif ch == 'L':          
        tess.left(90)
    
    elif ch == 'S':          
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50) 
        tess.left(90)
    else:                    #for any other character, print an error message
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked