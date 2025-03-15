# https://pypi.org/project/colorgram.py/        --colorgram package

import colorgram
from turtle import Turtle , Screen
import turtle as t
import random
# Extract 6 colors from an image.
# colors = colorgram.extract('/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY18/image.jpg', 10)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     list.append(rgb)

# print(list)

list1 = [(247, 241, 234), (249, 228, 236), (224, 242, 230), (243, 236, 68), (183, 75, 21), (228, 154, 7), (234, 72, 134), (200, 163, 114), (216, 228, 238), (202, 131, 191)]

t.colormode(255)
tim=t.Turtle()


tim.speed(10)
tim.penup()

tim.setheading(180)
tim.forward(300)
tim.setheading(270)
tim.forward(250)
tim.setheading(360)
tim.hideturtle()


no_of_dots=100

for i in range(1, no_of_dots+1):
    tim.dot(10,(random.choice(list1)))
    tim.forward(50)

    if i % 10 ==0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)













my_screen=Screen()
my_screen.exitonclick()