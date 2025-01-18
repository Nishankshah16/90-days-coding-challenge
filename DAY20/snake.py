from turtle import Turtle, Screen
import time

screen=Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Saap sheedi The ultimate Nokia game!!!!!")
screen.tracer(0)
inital_xcorr=[0,-20,-40]
segment=[]


# angela's method
starting_position=[(0,0),(-20,0),(-40,0)]

for i in starting_position:
    new_turtle=Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(i)
    segment.append(new_turtle)


########################

# my method
# for i in range(3):
#     new_turtle=Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.goto(x=inital_xcorr[i],y=0)


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segment:
        seg.forward(10)
        
















screen.exitonclick()