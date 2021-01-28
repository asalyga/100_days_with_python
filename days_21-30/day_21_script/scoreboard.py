from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest = data.read()
            self.highest_score = self.highest
        self.color("White")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score : {self.score} Highest Score {self.highest_score}", align="center", font=("Arial", 25, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=f"Score : {self.score} Highest Score {self.highest_score}", align="center",
                   font=("Arial", 25, "normal"))

    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highest_score))

        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()




    #def set_highest(self):
    #    # read
    #    with open("data.txt") as file:
    #        highest = file.read()
    #        self.highest_score = highest
