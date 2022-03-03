from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

# Todo : 1. Create the screen 800*600 / back

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

# Todo : 2. Create and move a paddle
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball(0, 0)
scoreboard = Scoreboard()

screen.onkey(fun=r_paddle.paddle_up, key="Up")
screen.onkey(fun=r_paddle.paddle_down, key="Down")
screen.onkey(fun=l_paddle.paddle_up, key="w")
screen.onkey(fun=l_paddle.paddle_down, key="s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # if the ball hits the UP or DOWN -> change the y_direction
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # if the ball hits the paddle -> change the x_direction  AND  ball.speed goes up
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
        ball.speed_up()

    # if the ball hits the wall -> restart and change the direction
    if ball.xcor() > 380:
        scoreboard.l_score += 1
        scoreboard.show_score()
        ball.reset_position()
        # time.sleep(1)
    if ball.xcor() < -380:
        scoreboard.r_score += 1
        scoreboard.show_score()
        ball.reset_position()
        # time.sleep(1)

screen.exitonclick()
