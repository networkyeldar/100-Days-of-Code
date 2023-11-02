from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("my_file.txt") as file:
            self.highscore = int(file.read())

        self.goto(-100,260)
        self.color("white")
        self.write(f"Score: {self.score}  High Score: {self.highscore}", font=("Arial", 14, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("my_file.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", font=("Arial", 14, "normal"))

