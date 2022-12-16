from turtle import Turtle
import random

BALL_SPEED = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.setheading(random.randint(-30, 30))

    def move(self):
        self.forward(BALL_SPEED)

    def bounce_top_bottom_walls(self):
        self.setheading(-self.heading())

    def bounce_left_right_walls(self):
        self.setheading((180 - self.heading()) % 360)
