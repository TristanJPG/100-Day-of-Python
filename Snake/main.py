from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600) # 600 pixels by 600 pixels
screen.bgcolor("black") # background color
screen.title("Snake!") 
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")




gameisOn = True
while gameisOn:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        score.add_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for turtle in snake.allTurtle:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()