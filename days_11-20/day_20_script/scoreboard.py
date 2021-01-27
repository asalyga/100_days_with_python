from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Current level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER!", align="center", font=FONT)