import turtle
# from src.init import *
# from src.config import N

# Global constants
TOWER_THICKNESS = 10
PLATE_THICKNESS = 20
BASE_WIDTH = 0
SPACE_BETWEEN_TOWERS = 0

# Function to draw an empty board with the possibility of accommodating n towers
def drawBoard(n):
    global BASE_WIDTH
    global SPACE_BETWEEN_TOWERS

    # Configuring the Turtle Window
    win = turtle.Screen()
    win.bgcolor("white")
    win.title("Hanoi Towers")

    # Adjusted constants
    BASE_WIDTH = 2 * (n + 1) * (TOWER_THICKNESS + PLATE_THICKNESS)
    BOARD_HEIGHT = 2 * (TOWER_THICKNESS + PLATE_THICKNESS)

    # Initialize the turtle
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.penup()

    # Draw the board
    drawer.goto(-BASE_WIDTH/2, -BOARD_HEIGHT/2 - 150)
    drawer.pendown()
    drawer.pensize(2)

    for _ in range(2):
        drawer.forward(BASE_WIDTH)
        drawer.left(90)
        drawer.forward(BOARD_HEIGHT)
        drawer.left(90)

    # Draw the towers with equal spaces
    SPACE_BETWEEN_TOWERS = BASE_WIDTH / (n + 1)

    for i in range(n):
        drawer.penup()
        x_position = -BASE_WIDTH/2 + (i + 1) * SPACE_BETWEEN_TOWERS - TOWER_THICKNESS / 2
        drawer.goto(x_position, -150)
        drawer.pendown()
        drawer.pensize(2)

        for _ in range(n + 1):
            drawer.pendown()
            drawer.forward(PLATE_THICKNESS)
            drawer.left(90)
            drawer.forward(2 * (n + 1) * PLATE_THICKNESS)
            drawer.left(90)
            drawer.penup()  
    turtle.done()
    return win

drawBoard(3)

# Function to draw a disc at a specific position on the board
def drawDisc(nd, board, n):
    # Configuration constants
    TOWER_THICKNESS = 10
    PLATE_THICKNESS = 20

    # Initialize the turtle for drawing the disc
    disc_drawer = turtle.Turtle()
    disc_drawer.speed(0)
    disc_drawer.penup()

    # Find the tower and disk position on the board
    tower_index = None
    disk_index = None

    for i in range(len(board)):
        if nd in board[i]:
            tower_index = i
            disk_index = board[i].index(nd)
            break

    # Calculate the coordinates to draw the disk
    x_position = tower_index * (TOWER_THICKNESS + PLATE_THICKNESS)
    y_position = disk_index * PLATE_THICKNESS

    # Move the turtle to the calculated position
    disc_drawer.goto(x_position, y_position)

    # Draw the disk
    disc_drawer.pendown()
    disc_drawer.pensize(2)

    disc_drawer.forward(PLATE_THICKNESS)
    disc_drawer.left(90)
    disc_drawer.forward(2 * (n + 1) * PLATE_THICKNESS)
    disc_drawer.left(90)
    disc_drawer.forward(PLATE_THICKNESS)
    disc_drawer.left(90)
    disc_drawer.forward(2 * (n + 1) * PLATE_THICKNESS)
    disc_drawer.left(90)

    turtle.done()

# Example usage
drawDisc(2, [[3, 2], [1], []], 3)