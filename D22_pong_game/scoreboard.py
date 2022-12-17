from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self, position, draw_net=True):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(position)
        self.score = 0
        self.score_refresh()

    def score_refresh(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_refresh()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER :(", align=ALIGNMENT, font=FONT)
