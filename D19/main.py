from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color_list = ["red", "green", "purple", "cyan", "blue", "orange"]
user_bet = screen.textinput(
    title="Make your bet", prompt="Bet which turtle color will win!"
)

for index, color in enumerate(color_list):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-230, -125 + 50 * index)


def move_forward():
    turtle.forward(50)


def move_backward():
    turtle.backward(50)


def rotate_cloclkwise():
    turtle.setheading(turtle.heading() + 10)


def rotate_counter_cloclkwise():
    turtle.setheading(turtle.heading() - 10)


def reset():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


# screen.listen()
# screen.onkey(key="z", fun=move_forward)
# screen.onkey(key="a", fun=move_backward)
# screen.onkey(key="b", fun=rotate_cloclkwise)
# screen.onkey(key="n", fun=rotate_counter_cloclkwise)
# screen.onkey(key="c", fun=turtle.clear)
screen.exitonclick()
