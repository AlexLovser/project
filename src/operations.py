from src.config import *
from src.init import posDisque


def moveDisque(P, de, a):
    P[a].append(P[de].pop())


def towerBasePosition(context, tower_number):
    W = context['window_width']
    H = context['window_height']

    x = int(W / (N + 1) * (tower_number + 1) - W / 2 - TOWER_WIDTH / 2)
    y = -int(H * 0.4) + int(H * 0.2 / 2)

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
    drawer.goto(-int(W / 2), -int(H * 0.4))
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

        # drawer.penup()
        # drawer.goto(x, y - WINDOW_MARGIN - LITTLE_FONT_SIZE)
        # drawer.pendown()


def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def adjust_color_lighten(r, g, b, factor):
    return rgb_to_hex(
        int(255 - (255 - r) * (1 - factor)),
        int(255 - (255 - g) * (1 - factor)),
        int(255 - (255 - b) * (1 - factor))
    )


def adjust_color_darken(r, g, b, factor):
    return rgb_to_hex(r * factor, g * factor, b * factor)


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


def mouse_hovers_this_disk(context, disk_box):
    mx = context['mouse_x'] - context['window_width'] / 2
    my = -context['mouse_y'] + context['window_height'] / 2

    inx = ((disk_box[0] + 10) <= mx <= (disk_box[2] + 10))
    iny = ((disk_box[1] + 5) > my > (disk_box[3] - 5))

    return inx and iny


def disk_is_in_a_towers_space(context, ):
    mx = context['mouse_x'] - context['window_width'] / 2
    my = -context['mouse_y'] + context['window_height'] / 2
    TOWER_HEIGHT = (context['disk_number'] + 2) * DISK_HEIGHT
    
    disk_width = getDiskWidth(context, context['dragging'][0])
    disk_x = mx - context['dragging'][1][0]
    disk_y = my + context['dragging'][1][1]
    disk_box = (disk_x, disk_y + int(DISK_HEIGHT / 2), disk_x + disk_width, disk_y - DISK_HEIGHT)
    

    for i in range(N):
        x, y = towerBasePosition(context, i)
        tower_box = (x - TOWER_WIDTH / 2, y + TOWER_HEIGHT, x + TOWER_WIDTH / 2, y)

        x1, y1, x2, y2 = disk_box
        x3, y3, x4, y4 = tower_box

        if x3 < x2 and x4 > x1 and y4 < y1 and y3 > y2:
            return i


def drawDisc(drawer, context, disk_number, board):
    drawer.pensize(DISK_HEIGHT)
    drawer.penup()

    dragging = context['dragging']
    disk_position = posDisque(board, disk_number)
    disk_width = getDiskWidth(context, disk_number)
    
    if dragging and dragging[0] == disk_number:
        x = context['mouse_x'] - int(context['window_width'] / 2) - dragging[1][0]
        y = -context['mouse_y'] + int(context['window_height'] / 2) + dragging[1][1]
        drawer.color(context['disk_colors_adjusted'][disk_number])
    else:
        x, y = towerBasePosition(context, disk_position[0])

        x -= int(disk_width / 2)
        y += DISK_HEIGHT * disk_position[1] + int(DISK_HEIGHT / 2)

        disk_box = (x, y + int(DISK_HEIGHT / 2), x + disk_width, y - DISK_HEIGHT)

        is_hovered = mouse_hovers_this_disk(context, disk_box)

        if is_hovered:
            drawer.color(context['disk_colors_adjusted'][disk_number])
        else:
            drawer.color(context['disk_colors'][disk_number])
    

    drawer.goto(x, y)
    drawer.pendown()
    drawer.goto(x + disk_width, y)

    


    

