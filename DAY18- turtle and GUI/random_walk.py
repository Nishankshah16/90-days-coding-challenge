from turtle import Turtle , Screen
import random
import turtle as t


tim=Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed(10)
color =["red", "green","yellow","blue","orange","black","brown","grey","cyan","purple","violet"]
directions=[0, 90, 180, 270]
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b



for _ in range(0,200):
    tim.forward(20)
    tim.setheading(random.choice(directions))
    tim.pencolor(random_color())


screen=Screen()

screen.exitonclick()




