"""EXO4 Turtle Tutorial."""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -100)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

colormode(255)

leo.color(23, 20, 225)

leo.begin_fill()
leo.fillcolor(225, 20, 225)
leo.end_fill()

# Sets the turtle's speed

leo.speed(50)

# Hides the turtle at the end of the run

leo.hideturtle()
