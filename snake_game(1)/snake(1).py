import turtle
import time
import random
import winsound

class snake:
    def __init__(self, x, y, color, segment_color, keys):
        self.x = x
        self.y = y
        self.length = 1
        # Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color(color)
        self.segment_color = segment_color
        self.head.penup()
        self.head.goto(self.x,self.y)
        self.head.direction = "stop"
        self.segments = []
        self.keys = keys
        self.score = 0



    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_length(self, length):
        self.length = length

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_length(self):
        return self.length
    
    def get_score(self):
        return self.score

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    

    def go_down(self):
       if self.head.direction != "up":
            self.head.direction = "down"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"


    def event_handler(self, key):
        if key == self.keys[0]:
            self.go_up()
        if key == self.keys[1]:
            self.go_down()
        if key == self.keys[2]:
            self.go_left()
        if key == self.keys[3]:
            self.go_right()
       

    def checkWallCollision(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            self.head.goto(self.x, self.y)
            self.head.direction = "stop"
        
            # Hide the remaining body
            for segment in self.segments:
                segment.goto(1000, 1000)

            # Clear segments list
            self.segments = []

            # Clear Score
            self.score = 0


    def checkFoodCollision(self, food):
        if self.head.distance(food) < 20:
            # Move food to a random spot on the screen
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.count += 1
            food.goto(x, y)
            winsound.PlaySound("Vine Boom Sound Effect", winsound.SND_ASYNC)

            # Increase length of snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color(self.segment_color)
            new_segment.penup()
            self.segments.append(new_segment)
            self.score += 1





    def updateSegments(self):
        
        # Move the end segments first in reverse order
        for index in range(len(self.segments)-1, 0, -1):
            x = self.segments[index-1].xcor()
            y = self.segments[index-1].ycor()
            self.segments[index].goto(x, y)
    
        # Move segment 0 to where the head is
        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)


    def checkBodyCollision(self):
       
        # Body Collisions
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                self.head.goto(self.x, self.y)
                self.head.direction = "stop"
            # Hide the remaining body
                for segment in self.segments:
                    segment.goto(1000, 1000)

            # Clear segments list
                self.segments = []
                self.score = 0
