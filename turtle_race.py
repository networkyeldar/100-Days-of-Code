from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
screen.setup(500,400)
colors = ["red", "green", "blue", "purple", "black", "pink"]
y = -100
pace = [0, 5, 10, 15]
all_turtles = []
user_bet = screen.textinput(title="Make your bed", prompt="Which turtle win? Type color")
for turle_index in range(6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[turle_index])
    tim.penup()
    tim.goto(-230,y)
    all_turtles.append(tim)
    y += 50

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    random_turtle = random.choice(all_turtles)
    random_turtle.forward(random.choice(pace))
    if random_turtle.xcor() > 230:
        winner = random_turtle
        is_race_on = False
        if user_bet == winner.pencolor():
            print("You win!")
        else:
            print(f"You lost! The {winner.pencolor()} turtle won")
screen.exitonclick()
