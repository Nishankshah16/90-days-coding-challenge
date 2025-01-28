FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level: {self.level}",align="left",font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",font=FONT,align="center")


    def increase_level(self):
        self.level+=1
        pass