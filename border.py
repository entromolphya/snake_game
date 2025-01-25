from turtle import *


class Border(Turtle):
    def __init__(self):
        super().__init__()
        # self.border = []
        self.arrange_border_x(-300, 300)
        self.arrange_border_x(-300, -292)
        self.arrange_border_y(-300, -300)
        self.arrange_border_y(292, -300)

    def arrange_border_x(self, x, y):
        for i in range(0, 600, 25):
            bdr = Turtle("square")
            bdr.color("bisque1")
            bdr.penup()
            bdr.goto(x + i, y)

    def arrange_border_y(self, x, y):
        for i in range(0, 600, 25):
            bdr = Turtle("square")
            bdr.color("bisque1")
            bdr.penup()
            bdr.goto(x, y + i)
