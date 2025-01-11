import turtle

def drawSquare(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def drawTriangle(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def drawHouse(size, square_color, triangle_color):
    drawSquare(size, square_color)
    
    turtle.forward(size)
    
    drawTriangle(size, triangle_color)
    
    turtle.penup()
    turtle.backward(size)
    turtle.pendown()

def moveTo(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def drawMultipleHouses(number_of_houses, size, spacing):
    for i in range(number_of_houses):
        moveTo(i * spacing, 0)
        drawHouse(size, 'blue', 'red')

turtle.speed('fast')
turtle.hideturtle()

drawMultipleHouses(5, 100, 150)

turtle.done()