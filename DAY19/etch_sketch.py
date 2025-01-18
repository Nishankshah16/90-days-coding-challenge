import turtle
from turtle import Turtle, Screen
import random

tim=Turtle()
tim.shape("turtle")
screen=Screen()

def forward_move():
    tim.forward(10)

def turnback():
    tim.backward(10)

def turn_left():
    tim.left(5)

def turn_right():
    tim.right(5)

def clear():
    tim.clear()

def bring_to_start():
    tim.reset()
screen.listen()


screen.onkey(forward_move,"w")
screen.onkey(turnback, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.onkey(bring_to_start, "q")
















screen.exitonclick()