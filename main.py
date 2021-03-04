#snakegame

import turtle
import time
import random
delay = 0.2

#score
s = 0
h_score = 0

#screen setup
w = turtle.Screen()
w.title("Slythering Snake")
w.bgcolor("black")
w.setup(width = 600, height = 600)
w.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 100)
head.direction = "stop"

#To move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

#keyboard listening
w.listen()
w.onkey(go_up, "w")
w.onkey(go_down, "s")
w.onkey(go_right, "d")
w.onkey(go_left, "a")

#food
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.shapesize(0.50, 0.50)
apple.goto(0, 0)

# Segments for snake body
segments = []

#score
p = turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.penup()
p.hideturtle()
p.goto(0, 260)
p.write("Score: 0   High Score: {}".format(h_score), align = "center", font= ("KristenITC", 24, "normal"))

#Maingame
while True:
    w.update()

    time.sleep(delay)
    if head.distance(apple) < 15: #moving food to random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)

        # adding new segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        segments.append(new_seg)

        #increase score
        s += 10
        if s > h_score:
            h_score = s

        p.clear()  # update to previous score
        p.write("Score: {}   High Score: {}".format(s, h_score), align="center", font=("KristenITC", 24, "normal"))


    for index in range(len(segments) - 1, 0, -1):  # moving segments along with head
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:  # moving segment to head's place
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1) #border collision
        head.goto(0, 0)
        head.direction = "stop"

        #hide segments
        for seg in segments:
            seg.goto(1000, 1000)

        #clear segments
        segments = []

        s = 0 #reset score
        p.clear() #update to previous score
        p.write("Score: {}   High Score: {}".format(s, h_score), align="center", font=("KristenITC", 24, "normal"))

    #body collision
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:  #hide segments
                seg.goto(1000, 1000)

            seg.clear()

            s = 0  # reset score
            p.clear()  # update to previous score
            p.write("Score: {}   High Score: {}".format(s, h_score), align="center", font=("KristenITC", 24, "normal"))

























