from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.total = 0
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.total}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.total += 1
        self.clear()
        self.write(arg=f"Score = {self.total}", align=ALIGNMENT, font=FONT)

