from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.move_up, "Up" )
screen.onkey(snake.move_down, "Down" )
screen.onkey(snake.move_left, "Left" )
screen.onkey(snake.move_right, "Right" )

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collison with food
    if snake.head.distance(food) < 15:
        food.new_location()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        is_game_over = True

    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_over = True

screen.exitonclick()
