from turtle import Turtle, Screen

class Scores(Turtle):
    def __init__(self, x, y):
        self.scores = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{self.scores}", font=("Courier", 80, "normal"))
    def adding(self):
        self.clear()
        self.scores += 1
    def update(self):
        self.write(f"{self.scores}", font=("Courier", 80, "normal"))
