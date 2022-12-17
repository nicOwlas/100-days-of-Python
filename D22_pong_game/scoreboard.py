from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.goto((-60, 200))
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto((60, 200))
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def score_left_increase(self):
        self.left_score += 1
        self.score_refresh()

    def score_right_increase(self):
        self.right_score += 1
        self.score_refresh()
