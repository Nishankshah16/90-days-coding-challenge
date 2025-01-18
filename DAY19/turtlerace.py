import turtle
from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(500,500)


is_race_on=False
userbet=screen.textinput(title="Make your bet", prompt="Please give the color of turtle: ")
colors=["blue","red","green","black","orange","pink"]
y_position=[0,-20,-40,20,40,60]
turtles=[]


# for i in name:
#     for j in colors:
#         print(i)
#         i=Turtle(shape="turtle")
#         i.color(j)



for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=y_position[i])
    turtles.append(new_turtle)


if userbet:
    is_race_on=True


while is_race_on:

    for i in turtles:

        if i.xcor()>230:
            is_race_on=False
            winning_color=i.pencolor()

            if userbet==winning_color:
                print(f"You win {winning_color} ")
            else:
                print(f"You lose the winning color is {winning_color}")
               

        i.forward(random.randint(0,10))
    




# nishank=Turtle(shape="turtle")
# nishank.penup()
# nishank.goto(x=-250,y=0)
# nishank.color("red")


# anuja=Turtle(shape="turtle")
# anuja.penup()
# anuja.goto(x=-250,y=20)
# anuja.color("blue")



# swaraj=Turtle(shape="turtle")
# swaraj.penup()
# swaraj.goto(x=-250,y=40)
# swaraj.color("green")


# abc=Turtle(shape="turtle")
# abc.penup()
# abc.goto(x=-250,y=60)
# abc.color("black")












screen.exitonclick()