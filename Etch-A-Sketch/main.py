from turtle import Turtle, Screen

Todd = Turtle()
screen = Screen()

def move_forward():
    Todd.forward(10)

def move_backwards():
    Todd.backward(10)
def counter_clockwise_turn():
    Todd.right(20)
def clockwise_turn():
    Todd.left(20)
def clear_drawing():
    Todd.reset()
screen.listen()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise_turn)
screen.onkey(key="d", fun=clockwise_turn)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()