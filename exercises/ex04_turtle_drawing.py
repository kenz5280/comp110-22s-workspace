"""A turtle drawing of a beautiful, multicolored flower."""

__author__ = "730489406"

from turtle import Turtle, colormode, done

from random import randint

colormode(255)

object: Turtle = Turtle()


def stem(stem: Turtle, x: float, y: float) -> Turtle:
    """A function to draw a stem."""
    stem.penup()
    stem.goto(x, y)
    stem.pendown()
    i: int = 0
    stem.begin_fill()
    while i < 2:
        stem.color(76, 123, 91)
        stem.forward(11)
        stem.right(90)
        stem.forward(250)
        stem.right(90)
        i += 1
        stem.fillcolor(76, 123, 91)
    stem.end_fill()
    stem.hideturtle()
    return(stem)


def petal(petal: Turtle, x: float, y: float) -> Turtle:
    """A function to draw the petals."""
    petal.penup
    petal.goto(x, y)
    petal.pendown
    i: int = 0
    while i < 7:
        n: int = 0
        petal.begin_fill()
        while n < 100:
            red: int = randint(0, 255)
            green: int = randint(0, 255)
            blue: int = randint(0, 255)
            petal.forward(1)
            petal.left(1)
            n += 1
            petal.color(red, green, blue)
            petal.fillcolor(red, green, blue)
        petal.end_fill()
        petal.penup
        petal.goto(x, y)
        i += 1
    petal.hideturtle()
    return(petal)


def center(center: Turtle, x: float, y: float) -> Turtle:
    """The drawing of the center of the flower."""
    center.penup()
    center.goto(x, y)
    center.pendown()
    i: int = 0
    center.begin_fill()
    while i < 360:
        center.forward(0.2)
        center.left(1)
        i += 1
        center.color(225, 195, 20)
        center.fillcolor(225, 195, 20)
    center.end_fill()
    center.hideturtle()   
    return center 


def right_leaf(right_leaf: Turtle, x: float, y: float) -> Turtle:
    """A function drawing a leaf."""
    right_leaf.penup()
    right_leaf.goto(x, y)
    right_leaf.setheading(350)
    right_leaf.pendown()
    right_leaf.begin_fill()
    right_leaf.fillcolor(10, 61, 26)
    i: int = 0
    while i < 120:
        right_leaf.forward(0.7)
        right_leaf.left(1)
        i += 1
        right_leaf.color(10, 61, 26)
    right_leaf.goto(x, y)
    right_leaf.end_fill()
    right_leaf.hideturtle()
    return right_leaf


def left_leaf(left_leaf: Turtle, x: float, y: float) -> Turtle:
    """A function drawing a leaf."""
    left_leaf.penup()
    left_leaf.goto(x, y)
    left_leaf.setheading(10)
    left_leaf.pendown()
    left_leaf.begin_fill()
    left_leaf.fillcolor(10, 61, 26)
    i: int = 0
    while i < 120:
        left_leaf.backward(0.7)
        left_leaf.right(1)
        i += 1
        left_leaf.color(10, 61, 26)
    left_leaf.goto(x, y)
    left_leaf.end_fill()
    left_leaf.hideturtle()
    return left_leaf


def main() -> None:
    """Main function."""
    object.speed(15) 
    stem(object, -5, -30)
    petal(object, 0, 0) 
    center(object, -3, -12)
    right_leaf(object, 6, -185)
    left_leaf(object, -5, -150)
    right_leaf(object, 6, -255)
    left_leaf(object, -5, -225)
    done()


if __name__ == "__main__":
    main()