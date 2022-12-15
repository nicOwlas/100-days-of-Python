from turtle import Turtle, Screen

INITIAL_POSITION = (-100, 0)
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        # Snake body
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for index in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(-20 * index + INITIAL_POSITION[0], INITIAL_POSITION[1])
            self.segments.append(segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[index - 1].pos()
            self.segments[index].setpos(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
