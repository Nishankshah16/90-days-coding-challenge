from turtle import Turtle, Screen

STARTING_POSITION=[0,-20,-40]
MOVE_DSITANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0




class Snake:
    #starting_position=[0,-20,-40]  why cant i write variable over here

    

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
        pass


    def create_snake(self):
        for i in STARTING_POSITION:
            new_turtle=Turtle("square")
            new_turtle.shapesize(1,1)
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x=i,y=0)
            self.segments.append(new_turtle)

    def move(self):

        for seg_num in range(len(self.segments)-1,0,-1):
            x_new = self.segments[seg_num-1].xcor()
            y_new= self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_new,y_new)
        
        self.head.forward(MOVE_DSITANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
