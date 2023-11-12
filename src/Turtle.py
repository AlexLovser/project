import turtle
from init import *
from config import N
from random import randint
colors = ["#1ecbe1", "#2684d9", "#2960d6", "#243ddb", "#3023dc", "#4823dc", "#6220df", "#831ee1"]

def drawBoard(n):
    turtle.update()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,150)
    turtle.pendown()
    turtle.color("white")
    turtle.write("Tour d'Hanoï",align="center",font=("ariel",48,"bold"))
    turtle.color("white")
    turtle.hideturtle()


    dr = turtle.Turtle()
    dr.speed(0)
    dr.penup()
    win = turtle.Screen()
    x, y = 900, 600

    win.setup(x,y)
    win.bgcolor("#8da11d")
    dr.color("white")
    dr.pensize(4)
    dr.goto(-x/2 + 50,-y/4)
    dr.pendown()
    turtle.update()


    for i in range (3):
        dr.forward(n * 25)
        dr.forward(-n * 12.5)
        dr.left(90)
        dr.forward(200)
        dr.forward(-200)
        dr.left(-90)
        dr.penup()
        dr.left(-90)
        dr.forward(25)
        dr.write(f"Tower #{i+1}",align="center",font=("ariel",14,"bold"))
        dr.forward(-25)
        dr.left(90)
        dr.forward(n * 25)
        dr.pendown()
    

    turtle.hideturtle()
    turtle.done()

def drawDisc(nd, board, n):
    turtle.update()
    disc_turtle = turtle.Turtle()
    disc_turtle.speed(0)
    disc_turtle.penup()
    disc_turtle.pensize(20)
    i in colors
    disc_turtle.pencolor(colors[i-1])
    tower_number = posDisque(board, nd)
    tower_height = nbDisques(board, tower_number)
    disc_size = n  + 1 
    x = (-400) + (nd*12 ) + ((nd-1) * 43) * 0# the final number is the tower number - 1
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
    tower_height = nbDisques(board, tower_number)
    for i in range(1,n+1):
        eraseDisc(i,board,n)
    drawBoard(n)

n=8
for i in range(1,n+1):
    drawDisc(n, init(n), i)
# drawBoard(n)
eraseDisc(1,init(8),8)

drawConfig(init(n),n)
# resetConfig(init(n),n)

