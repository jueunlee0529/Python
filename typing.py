from random import *
import turtle

house = turtle.Turtle()
line = turtle.Turtle()
t = turtle.Turtle(shape = "turtle")
line.goto(-50, 0)
line.goto(150, 0)

house.fillcolor("royalblue")
house.begin_fill()
house.end_fill()

t= turtle.Turtle()
g = turtle.Turtle()
g.write("씨큐브 코딩의 타자 게임!", True, font = ("Arial", 20, "bold"))
fruit = ["apple", "banana", "strawberry", "watermelon", "manderin",
         "peach", "grapes", "orange", "pear", "kiwi"]
score = 0
n = randint(5, 10)

for i in range(n) :
    s = choice(fruit)
    word = turtle.textinput("fruit", '%s(%d/%d)'%(s, i+1, n))
    if s == word :
        score += 1
rate = score/n*100

g.penup()
g.goto(0, -50)
g.pendown()

g.write("정확도 : %.1f%%"%rate, True, font = ("Arial", 15, "bold"))



        
