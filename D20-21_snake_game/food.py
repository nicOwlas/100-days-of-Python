from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.move()

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


# food = Food()
# print(food.pos())
