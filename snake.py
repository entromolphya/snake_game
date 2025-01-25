from turtle import *

set_positions = [(0, 0), (-20, 0), (-40, 0)]
mov_dis = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.snake = []

        for i in set_positions:
            a = Turtle("square")
            a.color("white")
            a.penup()
            a.goto(i)
            self.snake.append(a)

        self.head = self.snake[0]

        self.snake[1].color("chartreuse4")
        self.snake[2].color("red")

    def add_seg(self):
        a = Turtle("square")
        a.color("white")
        a.penup()
        a.goto(self.snake[-1].position())
        self.snake.append(a)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)

        self.snake[0].forward(mov_dis)

    def up_ward(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down_ward(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def turn_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def turn_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
