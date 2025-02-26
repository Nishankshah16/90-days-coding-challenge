from turtle import Turtle , Screen
import random
import turtle as t


tim=Turtle()
tim.shape("turtle")

tim.speed(20)
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b

def draw():
    tim.circle(100)
    tim.pencolor(random_color())

angle=5

for i in range(int(360/angle)):
    
    draw()
    tim.left(angle)
    
    



screen=Screen()

screen.exitonclick()




