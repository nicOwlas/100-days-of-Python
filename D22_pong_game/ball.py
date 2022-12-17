from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_move = random.randint(1, 10)
        self.y_move = random.randint(1, 10)
        self.speed = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_top_bottom_walls(self):
        self.y_move *= -1

    def bounce_left_right_walls(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move = random.randint(1, 10)
