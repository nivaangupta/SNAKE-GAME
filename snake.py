from turtle import Turtle


class Snake:
    def __init__(self):
        self.num_of_blocks = 3
        self.distance_between_blocks_center = 0
        self.snakes = []
        self.create_snake(self.num_of_blocks)
        self.head = self.snakes[0]

    def create_snake(self, num_of_blocks):
        for _ in range(num_of_blocks):
            snake = Turtle(shape="square")
            snake.penup()
            snake.color('white')
            snake.setposition(self.distance_between_blocks_center, 0)
            self.snakes.append(snake)
            self.distance_between_blocks_center -= 22

    def move(self):
        for index in range(len(self.snakes), 1, -1):
            self.snakes[index-1].goto(self.snakes[index-2].xcor(), self.snakes[index-2].ycor())
        self.snakes[0].forward(22)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def add_snake(self):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color('white')
        snake.setposition(self.snakes[len(self.snakes)-1].xcor(), self.snakes[len(self.snakes)-1].ycor())
        self.snakes.append(snake)

    def reset(self):
        for snake in self.snakes:
            snake.hideturtle()
        self.snakes.clear()
        self.distance_between_blocks_center = 0
        self.create_snake(3)
        self.head = self.snakes[0]
