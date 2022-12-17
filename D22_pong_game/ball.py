from turtle import Turtle
import random

BALL_SPEED = 4


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        angle_start = random.randint(-30, 30)
        self.tilt(-angle_start)
        self.setheading(angle_start)

    def move(self):
        self.forward(BALL_SPEED)

    def bounce_top_bottom_walls(self):
        bounce_angle = -self.heading()
        self.setheading(bounce_angle)
        self.tiltangle(0)

    def bounce_left_right_walls(self):
        bounce_angle = (180 - self.heading()) % 360
        self.setheading(bounce_angle)
        self.tiltangle(0)
