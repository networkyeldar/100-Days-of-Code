from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.forward(-10)
def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clean)
screen.exitonclick()
