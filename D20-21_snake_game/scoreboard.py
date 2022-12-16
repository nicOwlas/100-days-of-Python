from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.score = 0
        self.score_refresh()

    def score_refresh(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_refresh()

    def gameover(self):
        self.setpos(0, 0)
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)