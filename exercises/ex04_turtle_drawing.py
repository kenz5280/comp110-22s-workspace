"""A turtle drawing by me. Some beautiful flowers."""

__author__ = "730489406"

from turtle import Turtle, colormode, done

from random import randint

colormode(255)


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
            petal.begin_fill()
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
    stem(Turtle(), -5, -30)
    petal(Turtle(), 0, 0) 
    center(Turtle(), 0, -12)
    right_leaf(Turtle(), 2, -205)
    right_leaf(Turtle(), 2, -255)
    left_leaf(Turtle(), -5, -150)
    left_leaf(Turtle(), -5, -225)
    done()


if __name__ == "__main__":
    main()