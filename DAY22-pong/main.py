from turtle import Turtle, Screen
import random
from sidebars import Sidebar
from ball import Ball

my_screen=Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("Ping pong game")

my_screen.tracer(0)

sidebar1 = Sidebar((260,0))
sidebar2 = Sidebar((-260,0))
balls=Ball()



def middle_line():
    mid_turtle=Turtle()
    mid_turtle.color("white")
    mid_turtle.pensize(5)
    mid_turtle.hideturtle()
    mid_turtle.penup()
    mid_turtle.goto(0,-300)
    mid_turtle.pendown()
    mid_turtle.setheading(90)
    mid_turtle.goto(0,300)


my_screen.listen()
my_screen.onkey(sidebar1.go_up, "Up")
my_screen.onkey(sidebar1.go_down, "Down")
my_screen.onkey(sidebar2.go_up, "w")
my_screen.onkey(sidebar2.go_down, "s")








middle_line()
while True:
    my_screen.update()












my_screen.exitonclick()