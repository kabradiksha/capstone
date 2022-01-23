from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def is_finish(self):
        if self.ycor() > 280:
            return True
        return False

    def go_to_start(self):
        self.goto(0, -280)