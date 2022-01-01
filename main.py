from turtle import Turtle, Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

screen = Screen()
paddle_1 = Paddle(-350,0)
paddle_2 = Paddle(350,0)
scoreboard = Score()
ball = Ball()

screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

game_on = True

screen.listen()
screen.onkey(paddle_1.up,"Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up,"w")
screen.onkey(paddle_2.down, "s")
x = 0
y = 0 

while game_on:
  screen.update()
  ball.ball_move(x,y)

screen.exitonclick()