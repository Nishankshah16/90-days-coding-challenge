# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer        --tracer() method

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Saap sheedi The ultimate Nokia game!!!!!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()














screen.exitonclick()
