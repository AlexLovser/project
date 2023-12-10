from src.cheating.types.generic import create_type, type_wrapper
from datetime import datetime


StartGameButton = create_type('StartGameButton')()


def get_position(ctx):
    return 0, 0


def draw(self, drawer):
    x, y = get_position(self.context)

    is_hovered = self.hovers(self.context['mouse_x'], self.context['mouse_y'])

    btn_w = int(self.context['window_width'] / 4)
    btn_h = int(btn_w / 1.618)

    drawer.penup()
    drawer.color('yellow')
    drawer.pensize(int(btn_h / 2))
    drawer.goto(x - int(btn_w / 2), y)
    drawer.pendown()
    drawer.goto(x + int(btn_w / 2), y)
    drawer.penup()

    tri_size = int(btn_h / 3.8)
    half = int(tri_size / 2)

    drawer.color('#222222')
    drawer.pensize(4 + 2 * is_hovered)
    
    drawer.goto(x + half, y)
    drawer.pendown()
    drawer.goto(x - half, y - half)
    drawer.goto(x - half, y + half)
    drawer.goto(x + half, y)

   

def callback(self, context):
    self.context['start_time'] = datetime.now()
    self.context['page'] = 'game'

    


def hovers(self, mouse_x, mouse_y):
    mouse_x -= int(self.context['window_width'] / 2)
    mouse_y = -mouse_y + int(self.context['window_height'] / 2)

    x, y = get_position(self.context)

    btn_w = int(self.context['window_width'] / 5)
    btn_h = int(btn_w / 1.618)

    inx = (x - btn_w / 2) <= mouse_x <= (x + btn_w / 2)
    iny = (y - btn_h / 2) <= mouse_y <= (y + btn_h / 2)

    return inx and iny


StartGameButton.draw = type_wrapper(StartGameButton, draw)
StartGameButton.callback = type_wrapper(StartGameButton, callback)
StartGameButton.hovers = type_wrapper(StartGameButton, hovers)
