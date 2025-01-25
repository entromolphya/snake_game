from turtle import *
from snake import Snake
from food import Food
from scoreboard import Score
from border import Border
import time

title("Snake game")

setup(600, 600)
bgcolor("black")

tracer(0)

snake = Snake()
food = Food()
score = Score()
border = Border()

while True:
    update()
    time.sleep(0.08)

    snake.move()

    if snake.head.distance(food) < 15:
        food.food_pos()
        score.score_count()
        snake.add_seg()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        break
    f = 1
    for i in snake.snake[1:]:
        if snake.head.distance(i) < 15:
            score.game_over()
            f = 0
            break
    if f == 0:
        break

    listen()
    onkey(snake.up_ward, "w")
    onkey(snake.down_ward, "s")
    onkey(snake.turn_left, "a")
    onkey(snake.turn_right, "d")

exitonclick()
