# Snake Game by Derek Nguyen 4th Period

# Imports
import turtle
import time
import random
import winsound
from snake import snake
import functools
import math
from food import food

delay = 0.1

# Score Variables
score = 0
high_score = 0

# Setup (window)
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)
snakes = []




# Snake Class test
snake1 = snake(-50, 0, "black", "grey", ["w", "s", "a", "d"])
snake2 = snake(50, 0, "white", "black", ["t", "g", "f", "h"])
snake3 = snake(0, -50, "blue", "white", ["Up", "Down", "Left", "Right"])
snake4 = snake(0, 50, "pink", "purple", ["i", "k", "j", "l"])

snakes.append(snake1)
snakes.append(snake2)
snakes.append(snake3)
snakes.append(snake4)

# Player 2 head
#head2 = turtle.Turtle()
#head2.speed(0)
#head2.shape("square")
#head2.color("blue")
#head2.penup()
#head2.goto(50, 0)
#head2.direction = "stop"





# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)
food.direction = "stop"
food.count = 1



segments = []
segments2 = []


# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("S1: 0 S2: 0 S3: 0 S4: 0  HS: 0", align="center", font=("Courier", 24, "normal"))


def updateScore(): 
   
    pen.clear()
    pen.write("S1: {} S2: {} S3: {} S4: {}  HS: {}".format(snake1.score, snake2.score, snake3.score, snake4.score, high_score), align="center", font=("Courier", 24, "normal"))


# Keybinds
wn.listen()
#wn.onkeypress(go_up, "w")
#wn.onkeypress(go_down, "s")
#wn.onkeypress(go_right, "d")
#wn.onkeypress(go_left, "a")
for snake in snakes:
    for k in snake.keys:
        wn.onkeypress(functools.partial(snake.event_handler, k), key=k)

# Main loop
while True:
    wn.update()

        # Clear Score
        #pen.clear()
        #score = 0
        #pen.write("Score:  {}  High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        #delay = .1

    for snake in snakes:
        snake.checkWallCollision()
        snake.checkFoodCollision(food)
        if snake.score > high_score:
            high_score = snake.score
        snake.updateSegments()
        snake.move()
        snake.checkBodyCollision()
    updateScore()
    delay = 0.1 * math.pow(0.9, food.count)
    print(delay)
    if delay ==  0.015009463529699918:
        delay = 0.02058911320946491

     #      pen.clear()
     #   pen.write("Score:  {}  High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
#
#        # Decreasing Delay
#        delay *= .9

    time.sleep(delay)

wn.mainloop()


