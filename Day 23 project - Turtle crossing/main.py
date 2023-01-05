"""Turtle crossing game - Try to reach the finish line, using the 'Up' button """
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 35:
            game_is_on = False
            scoreboard.game_over()

    if player.reach_final_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    screen.update()

screen.exitonclick()
