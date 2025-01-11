from turtle import *

def drawSquare():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(90)
    end_fill()
    penup()
color("WhiteSmoke")
bgcolor("Red")

drawSquare()
forward(90)
drawSquare()
left(90)
drawSquare()
left(90)
drawSquare()

hideturtle()
done()