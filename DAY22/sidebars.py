from turtle import Turtle, Screen 


class Sidebar(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.color("white")
        self.goto(position)


    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(),y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(),y_cor)
    


        