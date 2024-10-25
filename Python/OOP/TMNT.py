from turtle import *
from random import randint
ypos = 115
for lane in range(5):
    lane = Turtle()
    lane.speed(1000)
    lane.color("black")
    lane.penup()
    lane.goto(-300, ypos)
    lane.pendown()
    lane.goto(300, ypos)
    lane.penup()
    lane.goto(-100,-100)
    ypos = ypos -30
ypos2=115
for lane in range(12):
    finish = Turtle()
    finish.speed(1000)
    finish.color("black")
    finish.penup()
    finish.right(90)
    finish.goto(300, ypos2)
    finish.pendown()
    finish.forward(5)
    finish.penup()
    finish.goto(-100,-100)
    ypos2 = ypos2 -10
ypos3 = 110
for lane in range(12):
    red = Turtle()
    red.speed(1000)
    red.color("red")
    red.penup()
    red.right(90)
    red.goto(300, ypos3)
    red.pendown()
    red.forward(5)
    red.penup()
    red.goto(-100,-100)
    ypos3 = ypos3 -10
leonardo = Turtle()
leonardo.color("blue")
leonardo.shape("turtle")
leonardo.penup()
leonardo.goto(-300, 100)
leonardo.pendown()

Donatello= Turtle()
Donatello.color("purple")
Donatello.shape("turtle")
Donatello.penup()
Donatello.goto(-300, 70)
Donatello.pendown()

Raphael= Turtle()
Raphael.color("red")
Raphael.shape("turtle")
Raphael.penup()
Raphael.goto(-300, 40)
Raphael.pendown()

Michaelangelo= Turtle()
Michaelangelo.color("orange")
Michaelangelo.shape("turtle")
Michaelangelo.penup()
Michaelangelo.goto(-300, 10)
Michaelangelo.pendown()

for movement in range(200):
    leonardo.forward(randint(1, 5))
    Michaelangelo.forward(randint(1, 5))
    Donatello.forward(randint(1, 5))
    Raphael.forward(randint(1, 5))


input("Press Enter To Close")

