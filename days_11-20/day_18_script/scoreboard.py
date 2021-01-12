from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 25, "normal"))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 25, "normal"))

    def end_game(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 25, "normal"))


