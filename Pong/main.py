from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

ball = Ball()
score = Scoreboard()
leftPaddle = Paddle((-350, 0))
rightPaddle = Paddle((350, 0))
screen.listen()

screen.onkeypress(rightPaddle.go_up, "Up")
screen.onkeypress(rightPaddle.go_down, "Down")

screen.onkeypress(leftPaddle.go_up, "e")
screen.onkeypress(leftPaddle.go_down, "s")


gameIsOn = True

while gameIsOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 
    # paddle collision
    if ball.distance(rightPaddle) < 80 and ball.xcor()> 320 or ball.distance(leftPaddle) < 80 and ball.xcor() < -320:
        ball.bounce_x()
    #right paddle miss
    if ball.xcor() > 380:
        ball.restart_ball()
        score.left_score()
    #left paddle miss
    if ball.xcor() < -380:
        ball.restart_ball()
        score.right_score()
        
screen.exitonclick()


