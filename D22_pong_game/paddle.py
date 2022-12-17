from turtle import Turtle

MOVE_SPEED = 30
PADDLE_HEIGHT = 160
PADDLE_WIDTH = 10


class Paddle(Turtle):
    def __init__(self, initial_position, up_key, down_key) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(
            stretch_wid=(PADDLE_HEIGHT / 20), stretch_len=(PADDLE_WIDTH / 20)
        )
        self.goto(initial_position)
        self.up_key = up_key
        self.down_key = down_key

    def move_up(self):
        self.setposition(self.xcor(), self.ycor() + MOVE_SPEED)

    def move_down(self):
        self.setposition(self.xcor(), self.ycor() - MOVE_SPEED)

    def is_ball_colliding(self, ball):
        if (
            abs(ball.xcor() - self.xcor()) < PADDLE_WIDTH
            and abs(ball.ycor() - self.ycor()) < PADDLE_HEIGHT / 2
        ):
            return True
