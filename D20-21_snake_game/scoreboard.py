from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.score = 0
        self.high_score = 0
        self.score_refresh()

    def reset(self):
        if self.score > self.high_score:
            print(f"Congrats, {self.score} is a new high score!")
            self.high_score = self.score
        self.score = 0
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(
            f"Score:{self.score} - High score:{self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def score_increase(self):
        self.score += 1
        self.score_refresh()
