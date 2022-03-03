import turtle
import time
import random
import winsound

class food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(x,y)
        self.food.direction = "stop"
        self.count = 1

    def reset(self):
        # Move food to a random spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.count += 1
        self.food.goto(x, y)
        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)
