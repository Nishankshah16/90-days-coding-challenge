import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()



player= Player()
car_manger=CarManager()
score=Scoreboard()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:

    time.sleep(0.1) 
    screen.update()

    car_manger.generate_car()
    car_manger.move_cars()

    #detect collsion

    for car in car_manger.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            # player.write("Game over",font=("areial",20,"normal"))
            score.game_over()
        

    if player.is_at_finsh_line():
        player.go_to_start()
        car_manger.level_up()
        score.increase_level()
        score.update_score()


    

screen.exitonclick()
              
