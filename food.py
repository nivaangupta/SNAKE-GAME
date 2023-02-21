from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.num_of_food_eaten = 0
        self.color("blue")
        self.penup()
        self.shapesize(.5, .5)
        self.speed("fastest")
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)

    def collision(self, snake):
        if self.distance(snake) < 15:
            self.goto(random.randint(-275, 275), random.randint(-275, 275))
            self.num_of_food_eaten += 1
            return True





