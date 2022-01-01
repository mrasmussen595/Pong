from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, position_1, position_2):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,0.75,1)
        self.goto(position_1, position_2)


    def up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(),new_y)