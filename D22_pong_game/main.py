from turtle import Screen
from paddle import Paddle
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

paddle_1 = Paddle(initial_position=(-360, 0), up_key="a", down_key="q")
paddle_2 = Paddle(initial_position=(360, 0), up_key="Up", down_key="Down")

paddles = [paddle_1, paddle_2]

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
for paddle in paddles:
    screen.onkey(key=paddle.up_key, fun=paddle.move_up)
    screen.onkey(key=paddle.down_key, fun=paddle.move_down)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
