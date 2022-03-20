from turtle import Turtle

# constant variables
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# create snake body
class Snake:
    def __init__(self):
        self.x = 0
        self.segments = []
        for _ in range(3):
            snake = Turtle()
            snake.shape("square")
            snake.penup()
            snake.setpos(x=self.x, y=0)
            snake.color("white")
            self.x -= 20
            self.segments.append(snake)
        self.head = self.segments[0]

    def extend(self):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        last_position = self.segments[-1].position()
        snake.setpos(last_position)
        snake.color("white")
        self.segments.append(snake)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            prev_x = self.segments[num - 1].xcor()
            prev_y = self.segments[num - 1].ycor()
            self.segments[num].goto(prev_x, prev_y)
        self.segments[0].forward(20)
