from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.07
    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)
    
    def bounce_y(self):
        self.yMove *= -1
        
    def bounce_x(self):
        self.xMove *= -1
        self.moveSpeed *= 0.86
    
    def restart_ball(self):
        self.goto(0, 0)
        self.moveSpeed = 0.07
        self.bounce_x()
        