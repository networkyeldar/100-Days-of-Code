from turtle import Turtle
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-50, 260)
        self.write(f"Level:{self.level}",align="left", font=FONT)

    def game_over(self):
        self.goto(-50,0)
        self.write("Game Over.", font=FONT)

    def increse_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)
