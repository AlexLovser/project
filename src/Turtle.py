import turtle
from init import *
from config import N
from random import randint
colors = ["#1ecbe1", "#2684d9", "#2960d6", "#243ddb", "#3023dc", "#4823dc", "#6220df", "#831ee1"]


def drawDisc(nd, board, n, color):
    turtle.update()
    disc_turtle = turtle.Turtle()
    disc_turtle.speed(0)
    disc_turtle.penup()
    disc_turtle.pensize(20)
    disc_turtle.pencolor(colors[i-1])
    tower_number = posDisque(board, nd)
    tower_height = nbDisques(board, tower_number)
    disc_size = n  + 1 
    x = -400 + nd * 12 # + ((nd - 1) * 43) * 0 # the final number is the tower number - 1
    y = -133 - n * 21 + 20 * tower_height
    
    disc_turtle.goto(x , y)
    disc_turtle.pendown()
    disc_turtle.forward(disc_size)
    disc_turtle.forward(n * 10)
    disc_turtle.forward(-2 * n * 10)

    disc_turtle.penup() 
    turtle.update()
    disc_turtle.hideturtle()

def eraseDisc(nd, board, n):
    eraseTurtle = turtle.Turtle()
    eraseTurtle.speed(0)
    eraseTurtle.pencolor("#8da11d")
    eraseTurtle.penup()
    eraseTurtle.pensize(20)
    tower_number = posDisque(board, nd)
    tower_height = nbDisques(board, tower_number)
    disc_size = n  + 1 
    x = (-400) + (n*12 ) + ((n-1) * 43) * 0# the final number is the tower number - 1
    y = -133 - nd * 21 + 20 * tower_height
    eraseTurtle.goto(x , y)
    eraseTurtle.pendown()
    eraseTurtle.forward(disc_size)
    eraseTurtle.forward(n * 10)
    eraseTurtle.forward(-2 * n * 10)

    eraseTurtle.penup() 
    eraseTurtle.hideturtle()
    turtle.update()

def drawConfig(board, n):
    
    tower_number = posDisque(board, n)
    tower_height = nbDisques(board, tower_number)
    turtle.update()
    drawBoard(n)


def resetConfig(board, n):
    tower_number = posDisque(board, n)
    # tower_height = nbDisques(board, tower_number)
    
    for i in range(n):
        eraseDisc(i, board, n + 1)
    drawBoard(n)

n = 8
for i in range(n):
    drawDisc(n + 1, init(n + 1), i)

# drawBoard(n)
eraseDisc(1, init(8), 8)

drawConfig(init(n),n)
# resetConfig(init(n),n)

