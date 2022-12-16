from turtle import Turtle

MOVE_SPEED = 20


class Paddle(Turtle):
    def __init__(self, initial_position, up_key, down_key) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.goto(initial_position)
        self.up_key = up_key
        self.down_key = down_key

    def move_up(self):
        self.setposition(self.xcor(), self.ycor() + MOVE_SPEED)

    def move_down(self):
        self.setposition(self.xcor(), self.ycor() - MOVE_SPEED)
