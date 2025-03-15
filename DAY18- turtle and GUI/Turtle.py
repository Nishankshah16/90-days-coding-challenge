# https://trinket.io/docs/colors        --trinket colors
# https://docs.python.org/3/library/turtle.html         --turtle graphics docs
# https://cs111.wellesley.edu/reference/colors          --turtle colors

from turtle import Turtle , Screen
import random


tim=Turtle()
tim.shape("turtle")
color =["red", "green","yellow","blue","orange","black","brown","grey","cyan","purple","violet"]

def draw(sides):
    angle = 360/sides
    for i in range(sides):

        tim.forward(50)
        tim.right(angle)

for i in range(3, 11):
    tim.color(random.choice(color))
    draw(i)


screen=Screen()
screen.exitonclick()




