from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180
class Snake:
    def __init__(self):
        self.allTurtle = []
        self.make_snake()
        self.head = self.allTurtle[0]
        
    
        
    def make_snake(self):
        for turtlePosition in POSITION:
            self.add_turtle(turtlePosition)
    
    def add_turtle(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.allTurtle.append(t)
    
    def reset(self):
        for t in self.allTurtle:
            t.goto(1000, 1000)
        self.allTurtle.clear()
        self.make_snake()
        self.head = self.allTurtle[0]
  
        
    def extend(self):
        self.add_turtle(self.allTurtle[-1].position())
    
    
    def move_snake(self):
        for turtles_num in range(len(self.allTurtle) - 1 , 0 ,-1):
            newX = self.allTurtle[turtles_num - 1].xcor()
            newy = self.allTurtle[turtles_num - 1].ycor()
            self.allTurtle[turtles_num].goto(newX, newy)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    




    
    