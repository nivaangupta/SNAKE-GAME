from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


game_is_on = True
screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

python = Snake()
ball = Food()
board = Score()

screen.onkey(python.up, "Up")
screen.onkey(python.down, "Down")
screen.onkey(python.left, "Left")
screen.onkey(python.right, "Right")

while game_is_on:
    board.track_score(ball.num_of_food_eaten)
    time.sleep(0.2)
    screen.update()
    python.move()
    if ball.collision(python.head):
        python.add_snake()
    board.track_score(ball.num_of_food_eaten)
    board.score_process(ball.num_of_food_eaten)

    if python.head.xcor() > 290 or python.head.xcor() < -290 or python.head.ycor() > 290 or python.head.ycor() < -290:
        board.highscore_change(ball.num_of_food_eaten)
        board.game_over(ball.num_of_food_eaten)
        ball.num_of_food_eaten = 0
        python.reset()
        time.sleep(2.5)

    for snake in python.snakes[1:]:
        if python.head.distance(snake) < 10:
            board.highscore_change(ball.num_of_food_eaten)

            ball.num_of_food_eaten = 0
            python.reset()
            time.sleep(2.5)


screen.exitonclick()
