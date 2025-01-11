import turtle

def drawPlanet(size, color):

    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

drawPlanet(100, 'Green')