
# imports

import turtle
import winsound
import random
import time

# Setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align ="center", font=("Courier", 24, "bold"))
score_a = 0
score_b = 0 


# Score
score_a = 0
score_b = 0

# End Screen
pencil = turtle.Turtle()
pencil.speed(0)
pencil.color("white")
pencil.penup()
pencil.hideturtle()
pencil.goto(0, 0)

# Functions
# Moving Paddle A up. 
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)

# Keybinds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    # Border Checking
    # Top and Bottom Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
#        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)

    if ball.ycor() < -283:
        ball.sety(-283)
        ball.dy *= -1
#        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)
    # Side Borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align ="center", font=("Courier", 24, "bold"))
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)



    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align ="center", font=("Courier", 24, "bold"))
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)



    # Paddle and Ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)        
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)        
        ball.setx(-340)
        ball.dx *= -1

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_a.ycor() > 248:
        paddle_a.sety(248)

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)

    if paddle_b.ycor() > 248:
        paddle_b.sety(248)

    # AI Player B
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 30:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 30:
        paddle_b_down()

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)

    if paddle_b.ycor() > 248:
        paddle_b.sety(248)

    # AI Player A
#    if paddle_a.ycor() < ball.ycor() and abs(paddle_a.ycor() - ball.ycor()) > 30:
#        paddle_a_up()
#    elif paddle_a.ycor() > ball.ycor() and abs(paddle_a.ycor() - ball.ycor()) > 30:
#        paddle_a_down()

#    if paddle_a.ycor() < -240:
#        paddle_a.sety(-240)

#    if paddle_a.ycor() > 248:
#        paddle_a.sety(248)

# Endgame
    if score_a is 2:
        pencil.goto(0, 0)
        pencil.write("Player A Wins!", align = "center", font = ("Courier", 50, "bold"))
        time.sleep(5)
        exit()

    if score_b is 2:
        pencil.goto(0, 0)
        pencil.write("Player B Wins!", align = "center", font = ("Courier", 50, "bold"))
        time.sleep(5)
        exit()
