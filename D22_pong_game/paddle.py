from turtle import Turtle


class Paddle:
    def __init__(self, initial_position, up_key, down_key) -> None:
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=4, stretch_len=0.5)
        self.paddle.goto(initial_position)
        self.up_key = up_key
        self.down_key = down_key
        pass

    def move_up(self):
        self.paddle.setposition(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.setposition(self.paddle.xcor(), self.paddle.ycor() - 20)
