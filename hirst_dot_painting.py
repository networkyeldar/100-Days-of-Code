from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.hideturtle()
t.colormode(255)
color_list = [(250, 245, 248), (236, 224, 80), (197, 7, 71),
              (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216)]

timmy.penup()
timmy.goto(-200,-100)
y = -100
rounds = 1
while rounds != 11:
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    y += 50
    timmy.goto(-200, y)
    rounds +=1


screen = Screen()
screen.exitonclick()
