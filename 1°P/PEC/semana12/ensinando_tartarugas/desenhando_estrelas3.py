from turtle import *
from random import *

def moveToRandomLocations():
    penup()
    setpos( randint(-400, 400), randint(-400, 400))
    pendown()


def drawStar(starSize, starColor):
    color(starColor)
    pendown()
    begin_fill()
    for side in range(5):
        left (144)
        forward(starSize)
    end_fill()
    penup()

bgcolor('MidnightBlue')

for estar in range(30):
    moveToRandomLocations()
    drawStar( randint(5,25), "White")

hideturtle()
done()