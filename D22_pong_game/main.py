from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_net():
    net = Turtle()
    net.color("white")
    net.speed("fastest")
    net.hideturtle()
    net.penup()
    net.goto(0, -300)
    net.setheading(90)
    for _ in range(SCREEN_HEIGHT // 20):
        net.pendown()
        net.forward(10)
        net.penup()
        net.forward(10)


screen = Screen()
screen.tracer(0)
draw_net()
paddle_1 = Paddle(initial_position=(-360, 0), up_key="a", down_key="q")
paddle_2 = Paddle(initial_position=(360, 0), up_key="Up", down_key="Down")
ball = Ball()
scoreboard = Scoreboard()

paddles = [paddle_1, paddle_2]

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.listen()
for paddle in paddles:
    screen.onkey(key=paddle.up_key, fun=paddle.move_up)
    screen.onkey(key=paddle.down_key, fun=paddle.move_down)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Detect collision with paddle
    for paddle in paddles:
        if paddle.is_colliding(ball):
            ball.bounce_left_right_walls()
            ball.speed += 1

    # Detect collision with the walls
    if abs(ball.ycor()) > 290:
        ball.bounce_top_bottom_walls()

    # Detect scoring condition
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.score_left_increase()
    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.score_right_increase()

screen.exitonclick()
