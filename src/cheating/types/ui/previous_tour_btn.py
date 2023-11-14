from src.cheating.types.generic import create_type, type_wrapper
from src.history import undo_last_movement


PreviousButton = create_type('PreviousButton')()


def get_position(ctx):
    W = ctx['window_width']
    H = ctx['window_height']
    x = int(W / 2) - 50
    y = int(H / 2) - 50

    return x, y


def draw(self, drawer):
    x, y = get_position(self.context)

    is_hovered = self.hovers(self.context['mouse_x'], self.context['mouse_y'])

    drawer.penup()
    drawer.color('#ffffff')
    drawer.pensize(5 + 5 * is_hovered)
    drawer.goto(x, y)
    drawer.pendown()

    btn_w = 50
    btn_h = 50

    # triangle
    drawer.goto(x - btn_w, y - int(btn_h / 2))
    drawer.goto(x, y - btn_h)
    drawer.goto(x, y)




def callback(self, context):
    undo_last_movement(context)


def hovers(self, mouse_x, mouse_y):
    mouse_x -= int(self.context['window_width'] / 2)
    mouse_y = -mouse_y + int(self.context['window_height'] / 2)

    x, y = get_position(self.context)

    btn_w = 50
    btn_h = 50

    x1 = x - btn_w
    y1 = y - int(btn_h / 2)

    x2 = x
    y2 = y - btn_h

    x3 = x
    y3 = y

    u = ((y2 - y3) * (mouse_x - x3) + (x3 - x2) * (mouse_y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    v = ((y3 - y1) *(mouse_x - x3) + (x1 - x3) * (mouse_y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    w = 1 - u  - v

    return 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1



PreviousButton.draw = type_wrapper(PreviousButton, draw)
PreviousButton.callback = type_wrapper(PreviousButton, callback)
PreviousButton.hovers = type_wrapper(PreviousButton, hovers)
