from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import score

my_screen=Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("The snake game")
my_screen.tracer(0)

snake=Snake()
food=Food()
scores=score()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")




is_game_on=True

while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    

    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()


my_screen.exitonclick()