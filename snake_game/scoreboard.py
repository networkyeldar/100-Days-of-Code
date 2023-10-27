from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-50,260)
        self.color("white")
        self.write(f"Score: {self.score}", font=("Arial", 14, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 14, "normal"))

    def game_over(self):
        self.penup()
        self.goto(-50, 0)
        self.write(f"Gameover!", font=("Arial", 20, "normal"))
