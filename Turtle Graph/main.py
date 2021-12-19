import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.penup()
#From Hirst Color Paint file using colorgram. 
colorList = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26), (235, 164, 190), (156, 25, 22), (20, 189, 230), (238, 169, 157), (162, 210, 182)]


tim.setheading(225) # Positions dots to beginning of art piece. 
tim.forward(250)
tim.setheading(0)
numOfDots = 100

for dotCounts in range(1, numOfDots + 1): #1 , 100 ∴ only goes to 1-99. to finish project +1 to make 1-100. 
    tim.hideturtle()
    tim.dot(20, random.choice(colorList)) 
    tim.forward(50)
    
    if dotCounts % 10 == 0: # if dot counts (1-100) divided by 10 has a remainder of zero, then run this:
        tim.showturtle() 
        tim.setheading(90) 
        tim.forward(50) # is the dot gap
        tim.setheading(180) 
        tim.forward(500) # beginning of line on a new row 
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()