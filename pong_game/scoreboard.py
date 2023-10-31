from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.penup()
        self.goto(-50, 260)
        self.write(f"Score:{self.left_score} | {self.right_score}",font=("Arial",14))


    def update_score(self):
        self.write(f"Score:{self.left_score} | {self.right_score}",font=("Arial",14))
