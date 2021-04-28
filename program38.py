#Name: Youssef Elsuradi
#Email: Youssef.elsuradi59@myhunter.cuny.edu

import turtle
def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist,
    to move the turtle and a color, col, to set the turtle's color.
    DO NOT CHANGE THE CODE IN THIS FUNCTION
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def nestedPolygon(t, length, sides):
    """
    Takes three parameters: a turtle a side length and the number of sides.
    The function does the following: if the length is greater than 10,
    it repeats sides times:  moves forward that length, turns 360/sides degrees.
    When that is completed, it calls nestedPolygon(t, length/2, sides).
    """
    
    if length > 10:
        for i in range(sides):
            t.forward(length)
            t.left(360/sides)
        nestedPolygon(t, length/2,sides)
    






def fractalPolygon(t, length, sides):
    """
    Takes three parameters: a turtle a side length and the number of sides.
    The function does the following: if the length is greater than 10,
    it repeats sides times:  moves forward that length, turns 360/sides degrees,
    and calls fractalPolygon(t, length/2, sides).
    """

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################

    if length > 10:
        for i in range(sides):
            t.forward(length)
            t.left(360/sides)
            fractalPolygon(t,length/2,sides)




def main():
    l = int(input('Enter length: '))
    s = int(input('Enter number of sides: '))

    #check there are enough sides to draw a polygon
    if s < 3:
        print("A polygon must have at least 3 sides.")
    else:
        tom = turtle.Turtle()
        setUp(tom, -100, "darkgreen")
        nestedPolygon(tom, l, s)

        tess = turtle.Turtle()
        setUp(tess, 100, "steelblue")
        fractalPolygon(tess, l, s)

if __name__ == "__main__":
     main()
