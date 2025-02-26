COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE
            
    def generate_car(self):
        random_chance=random.randint(0,6)
        if random_chance == 1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor= random.randint(-250,250)
            new_car.goto(300,y_cor)
            self.all_cars.append(new_car)
            
    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT




        

