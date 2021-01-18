from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scores import Scores
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(False)
paddle1 = Paddle(-350)
paddle2 = Paddle(350)
score1 = Scores(-100, 200)
score2 = Scores(100, 200)
ball = Ball()
screen.update()
screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")
is_on = True
while is_on:
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit()
    elif (ball.distance(paddle2) < 50 and ball.distance(0, 0) > 340) or (ball.distance(paddle1) < 50 and ball.xcor() < -340):
        ball.paddle()
    elif ball.xcor() > 350:
        ball.reset()
        ball.speedx()
        score1.adding()
        score1.update()
    elif ball.xcor() < -350:
        ball.reset()
        ball.speedx()
        score2.adding()
        score2.update()
    screen.update()







screen.exitonclick()