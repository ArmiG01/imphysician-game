from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.xspeed = 10
        self.speed(self.xspeed)
        self.penup()
        self.x = 10
        self.y = 10
    def move(self):
        newx = self.xcor() + self.x
        newy = self.ycor() + self.y
        self.goto(newx, newy)
    def hit(self):
        self.y *= -1

    def paddle(self):
        self.x *= -1
    def reset(self):
        self.goto(0, 0)
        self.x *= -1
    def speedx(self):
        if self.xspeed > 1:
            self.xspeed *= 0.9
            self.speed(self.xspeed)

