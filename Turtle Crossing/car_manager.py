from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
       # super().__init__()
        self.all_cars = []
        self.carSpeed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        randomChance = random.randint(1,6)
        if randomChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250, 250)
            newCar.goto(300, randomY)
            self.all_cars.append(newCar)
            
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.carSpeed)
    def level_up(self):
        self.carSpeed += MOVE_INCREMENT
