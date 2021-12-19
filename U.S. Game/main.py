import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

score = 0
guessedList = []
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()



while len(guessedList) < 50:
    answer = screen.textinput(title=f"{len(guessedList)}/50 correct!", prompt="What's a Name of a State?").capitalize()
  
    if answer == "Exit":
        missingStates = []
        for state in states:
            if state not in guessedList:
                missingStates.append(state)
        newData = pandas.Dataframe(missingStates)
        newData.to_csv("States_To_Learn.csv")
        break
    if answer in states:
        guessedList.append(answer)
        stateData = data[data.state == answer]
        x = int(stateData.x)
        y = int(stateData.y)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x,y)
        t.write(answer)
        





