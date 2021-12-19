import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()
screen.title("Crossy Turtle!")
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkeypress(player.go_up, "e")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_cars()
    carManager.move_cars()
    
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.finish_line():
        carManager.level_up()
        player.go_to_start()
        scoreboard.increase_level()
screen.exitonclick()