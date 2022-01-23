from turtle import Turtle

FONT =("courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-380,260 )
        self.update()

    def update(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)