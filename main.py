from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# basic setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.turn_up, "Up")
screen.onkeypress(snake.turn_down, "Down")
screen.onkeypress(snake.turn_left, "Left")
screen.onkeypress(snake.turn_right, "Right")

while True:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # check if snake is touching food
    if snake.head.distance(food) < 15:
        snake.extend()
        score.updateScore()
        food.refresh()

    # check if snake is touching the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score.game_over()
        break

    # Check if head is touching body or tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            break

# exit game
screen.exitonclick()
