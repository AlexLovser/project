import turtle
from init import *
from config import N
from random import randint
colors = ["red", "blue", "black", "yellow", "cyan", "pink", "green", "purple"]

def drawBoard(n):

    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,150)
    turtle.pendown()
    turtle.write("Tour d'Hanoï",align="center",font=("ariel",48,"bold"))
    turtle.hideturtle()

    dr = turtle.Turtle()
    dr.speed(0)
    dr.penup()
    win = turtle.Screen()
    win.setup(900,600)
    dr.goto(-400,-150)
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
    disc_turtle = turtle.Turtle()
    disc_turtle.speed(0)
    disc_turtle.penup()
    disc_turtle.pensize(20)
    i in colors
    disc_turtle.pencolor(colors[i-1])
    tower_number = posDisque(board, nd)
    tower_height = nbDisques(board, tower_number)
    disc_size = n  + 1 
    x = (-400) + (nd*12 ) + ((nd-1) * 43) * 1 # the final number is the tower number - 1
    y = -133 - n * 21 + 20 * tower_height
    
    disc_turtle.goto(x , y)
    disc_turtle.pendown()
    disc_turtle.forward(disc_size)
    disc_turtle.forward(n * 10)
    disc_turtle.forward(-2 * n * 10)

    disc_turtle.penup() 
    turtle.update()
    disc_turtle.hideturtle()
    
for i in range(1,9):
    drawDisc(8, init(8), i)
drawBoard(8)
