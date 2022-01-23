from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.tracer(0)
player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    #detect  collision with cars
    for i in car.all_cars:
        if i.distance(player) < 20:
            is_on = False
            scoreboard.game_over()

    #detect a successful crossing
    if player.is_finish():
        player.go_to_start()
        car.speed_up()
        scoreboard.increase_level()





screen.exitonclick()