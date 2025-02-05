from turtle import Turtle
ALIGNMENT="CENTER"
FONT="aerial"

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



