from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.color("red")
turtle.shape('turtle')
#turtle.pensize(10)
turtle.speed('fastest')

def forward_dashed(turtle, path_length, dash_length):
    pass
    dash_number = path_length // (dash_length*2)
    for _ in range(dash_length):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)

def draw_polygon(turtle, n, side_length):
    angle = 360 / n
    for i in range(n):
        turtle.forward(side_length)
        turtle.right(angle)

def random_color():
    r = random.uniform(0,1)
    g = random.uniform(0,1)
    b = random.uniform(0,1)
    return (r, g, b)

circle_gap = 2
for _ in range(360//circle_gap):
    turtle.pencolor(random_color())
    turtle.circle(100)
    turtle.setheading(turtle.heading()+circle_gap)
    #turtle.setheading(random.choice([0, 90, 180, 270]))
    # turtle.forward(30)

screen = Screen()
screen.exitonclick()
