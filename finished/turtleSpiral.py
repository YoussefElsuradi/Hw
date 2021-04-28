#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu



import turtle
wn = turtle.Screen()
stamp = int(input('how many stamps? '))

tess = turtle.Turtle()
tess.color('cyan')

tess.shape('arrow')
tess.penup()

steps = 10

for i in range(stamp):
    tess.stamp()
    if (i%2==0):
        steps = steps + 3
    tess.forward(steps)
    tess.right(24)
    
wn.exitonclick()