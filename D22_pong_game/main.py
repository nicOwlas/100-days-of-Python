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
score_1 = Scoreboard((-60, 200), draw_net=True)
score_2 = Scoreboard((60, 200), draw_net=True)

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
        if paddle.is_ball_colliding(ball):
            ball.bounce_left_right_walls()
            if paddle is paddle_1:
                score_1.score_increase()
            else:
                score_2.score_increase()

    # Detect collision with the walls
    if abs(ball.ycor()) > 290:
        ball.bounce_top_bottom_walls()

    # Detect game over condition
    if abs(ball.xcor()) > 390:
        score_1.game_over()
        is_game_on = False

screen.exitonclick()
