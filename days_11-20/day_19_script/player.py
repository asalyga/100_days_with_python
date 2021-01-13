from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fast")
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1)

    def move_up(self):
        pass

    def move_down(self):
        pass
