from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(width=500, height=400)
isRaceOn = False
userBet = screen.textinput(title="Make Your Bet!", prompt="Which Turtle Will Win? Enter A Color:" )
allTurtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

yPostions = [-80, -40, 0, 40, 80, 120]
for turtleIndex in range(0, 6):
    aTurtle = Turtle(shape="turtle")
    aTurtle.color(colors[turtleIndex])
    aTurtle.penup()
    aTurtle.goto(x=-230, y=yPostions[turtleIndex])
    allTurtles.append(aTurtle)
    
if userBet:
    isRaceOn = True
while isRaceOn:
    for turtles in allTurtles:
        if turtles.xcor() > 230:
            isRaceOn = False
            winningColor =  turtles.pencolor()
            if winningColor == userBet:
                print(f"You have won! The {winningColor} turtle won the race!")
            else:
                print(f"You have lost! The {winningColor} turtle won the race!")
        distance = random.randint(0, 10)
        turtles.forward(distance)
screen.exitonclick()