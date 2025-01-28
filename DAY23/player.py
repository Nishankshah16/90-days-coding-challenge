STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.make_turtle()
        pass
    
    def make_turtle(self):
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        ycor=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),ycor)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finsh_line(self):
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False
        
        



    

