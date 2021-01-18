from turtle import Screen, Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position, 200)
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)
    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

