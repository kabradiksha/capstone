from turtle import Turtle
import random

MOVE_INCREMENT = 5
CAR_SPEED = 5

COLORS = ["red", "green", "blue", "orange", "purple", "yellow"]

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_SPEED

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(400, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT