import turtle
from threading import Thread
from src.init import nbDisques, init


TOWER_THICKNESS = 10


def square(width, height, drawer):
    def inner():
        for _ in range(2):
            drawer.forward(width)
            drawer.left(90)
            drawer.forward(height)
            drawer.left(90)

    Thread(target=inner).start()



def render(P, turtles_set):
    n = len(turtles_set) - 1
    DISK_HEIGHT = 50
    BASE_WIDTH = 2 * len(turtles_set) * (TOWER_THICKNESS + DISK_HEIGHT)
    BASE_HEIGHT = 2 * (TOWER_THICKNESS + DISK_HEIGHT)
    SPACE_BETWEEN_TOWERS = BASE_WIDTH / (n + 1)
    TOWER_HEIGHT = 300
    TOWER_WIDTH = 25
    
    main_turtle = turtles_set[-1]
    main_turtle.goto(-BASE_WIDTH / 2, -BASE_HEIGHT / 2 - 185)
    main_turtle.pendown()

    square(BASE_WIDTH, BASE_HEIGHT, main_turtle)
    
    for i in range(n):
        drawer = turtles_set[i]
        drawer.penup()
        d = nbDisques(P, i)
        # for disk in ...

        drawer.goto(x_position, y_position)



        d = nbDisques(P, i) * DISK_HEIGHT
        x_position = -BASE_WIDTH / 2 + (i + 1) * SPACE_BETWEEN_TOWERS - TOWER_THICKNESS / 2
        y_position = -125 + d
        drawer.goto(x_position, y_position)
        drawer.pendown()
        
        square(TOWER_WIDTH, TOWER_HEIGHT - d, drawer)



def drawBoard(P, n):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Hanoi Towers")

    turtles_set = [turtle.Turtle() for _ in range(n + 1)]

    for i in turtles_set:
        i.speed(0)
        i.pensize(2)
        i.penup()

    render(P, turtles_set)

    turtle.done()
    return window

PLATEAU = init(3)

drawBoard(PLATEAU, 3)