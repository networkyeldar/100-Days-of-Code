from turtle import Turtle
STARTING_POSITION = (0, - 280)
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(0,-280)


    def move_player(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_that_finish_line(self):
        if self.ycor() > 270:
            return True
        else:
            return False
