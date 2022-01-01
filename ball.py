from turtle import Turtle, xcor
from score import Score
import random

class Ball(Turtle, Score):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.75,0.75,0.75)
        self.penup()

    def ball_move(self, i, x):
        new_x=self.xcor()+0.75
        new_y=self.xcor()+0.75
        self.goto(new_x, new_y)
        score = Score
        if self.xcor()>580:
            score.score_p1(i)
        elif self.xcor()<580:
            score.score_p1(x)
        elif self.ycor()>580 or self.ycor()<-580:
            self.setheading(380-self.heading)
