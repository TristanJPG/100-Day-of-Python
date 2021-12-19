import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors



tim.shape("turtle")

tim.speed("fastest")
def draw_sepriograh(sizeOfGap):
    for _ in range(int(360/sizeOfGap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + sizeOfGap)
        tim.circle(100)


draw_sepriograh(4)

screen = t.Screen()
screen.exitonclick()