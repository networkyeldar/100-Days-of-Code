from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


cars = Cars()
player = Player()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(player.move_player,"Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()
    if player.is_that_finish_line():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increse_level()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
