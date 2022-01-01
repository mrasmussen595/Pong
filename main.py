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

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

game_on = True

screen.listen()
screen.onkey(paddle_1.up,"Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up,"w")
screen.onkey(paddle_2.down, "s")
p1_score = 0
p2_score = 0 

scoreboard.score_write(p1_score,p2_score)

while game_on:
    screen.update()
    ball.move()
    
  

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
      ball.bounce_x()
    
    if ball.xcor()<-350:
      p2_score+=1
      scoreboard.score_write(p1_score,p2_score)
      ball.reset_position()

    if ball.xcor()>350:
      p1_score+=1
      scoreboard.score_write(p1_score, p2_score)
      ball.reset_position()
    
screen.exitonclick()