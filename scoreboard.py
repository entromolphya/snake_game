from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.current_score()

    def current_score(self):
        self.write(f"Your Score : {self.score}", False, "center", ("Ubuntu", 15, "bold"))

    def score_count(self):
        self.score += 1
        self.clear()
        self.current_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over \nYour final Score : {self.score}", False, "center", ("Ubuntu", 15, "bold"))
