from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake is back!")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ## Detect collision with food
    if food.distance(snake.head) <= 15:
        snake.extend()
        food.move()
        scoreboard.score_increase()

    ## Detect collisions
    if (
        abs(snake.head.xcor()) > 280
        or abs(snake.head.ycor()) > 280
        or snake.is_tail_colliding() is True
    ):
        scoreboard.gameover()
        game_is_on = False


screen.exitonclick()
