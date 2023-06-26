from turtle import Turtle
from turtle import Screen
from random import randint


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def make_screen(color, title, w, h):
    window = Screen()
    window.bgcolor(color)
    window.title(title)
    window.setup(width=w, height=h)
    return window


def change_food_position(food):
    x = randint(-270, 270)
    y = randint(-270, 270)
    food.goto(x, y)


def move_snake(snake_head):
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)
