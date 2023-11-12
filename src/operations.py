from src.config import *
from src.init import posDisque


def moveDisque(P, de, a):
    P[a].append(P[de].pop())


def towerBasePosition(context, tower_number):
    W = context['window_width']
    H = context['window_height']

    x = int(W / (N + 1) * (tower_number + 1) - W / 2 - TOWER_WIDTH / 2)
    y = -int(H / 2 * 0.8) + int(H * 0.2 / 2)

    return x, y


def getDiskWidth(context, ndisk):
    W = context['window_width']

    MAX_DISK_WIDTH = int(W / (N + 1) * 0.8 - TOWER_WIDTH / 2)
    MIN_DISK_WIDTH = int(W / (N + 1) * 0.2 - TOWER_WIDTH / 2)
    DELTA = MAX_DISK_WIDTH - MIN_DISK_WIDTH

    return MIN_DISK_WIDTH + int(DELTA / context['disk_number'] * (ndisk - 1))


def drawBoard(drawer, context):
    W = context['window_width']
    H = context['window_height']
    TOWER_HEIGHT = (context['disk_number'] + 2) * DISK_HEIGHT

    # BASE
    drawer.penup()
    drawer.goto(-int(W / 2), -int(H / 2 * 0.8))
    drawer.pendown()
    drawer.pensize(int(H * 0.2))
    drawer.forward(W)

    # TOWERS
    drawer.pensize(TOWER_WIDTH)
    
    for i in range(N):
        drawer.penup()

        x, y = towerBasePosition(context, i)
        
        drawer.goto(x, y)
        drawer.pendown()
        drawer.goto(x, y + TOWER_HEIGHT)

        drawer.penup()
        drawer.goto(x, y - WINDOW_MARGIN - LITTLE_FONT_SIZE)
        drawer.pendown()


def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def generateDiskColor(context, ndisk):
    coef = (ndisk - 1) / context['disk_number'] * len(RAINBOW)
    start = coef
    end = min((len(RAINBOW) - 1, start + 1))
    
    start_color = RAINBOW[int(start)]
    end_color = RAINBOW[int(end)]

    color = []

    for i in range(3):
        color.append(int(start_color[i] + (end_color[i] - start_color[i]) * (start - int(start))))

    return rgb_to_hex(*color)


def drawDisc(drawer, context, disk_number, board, color):
    drawer.pencolor(color)
    drawer.pensize(DISK_HEIGHT)
    drawer.penup()

    disk_position = posDisque(board, disk_number)
    disk_width = getDiskWidth(context, disk_number)

    x, y = towerBasePosition(context, disk_position[0])

    x -= int(disk_width / 2)
    y += DISK_HEIGHT * disk_position[1] + int(DISK_HEIGHT / 2)
    

    drawer.goto(x, y)
    drawer.pendown()
    drawer.goto(x + disk_width, y)

    


    

