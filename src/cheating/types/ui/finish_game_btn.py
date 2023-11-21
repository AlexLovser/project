from src.cheating.types.generic import create_type, type_wrapper
from src.history import undo_last_movement
from src.init import init


FinishGameButton = create_type('FinishGameButton')()


def get_position(ctx):
    W = ctx['window_width']
    H = ctx['window_height']
    x = -int(W / 2) + 25
    y = int(H / 2) - 25

    return x, y


def draw(self, drawer):
    x, y = get_position(self.context)

    is_hovered = self.hovers(self.context['mouse_x'], self.context['mouse_y'])

    drawer.penup()
    drawer.color('#ffffff')
    drawer.pensize(5 + 2 * is_hovered)
    drawer.goto(x, y)
    drawer.pendown()

    btn_w = 50
    btn_h = 50

    # triangle
    drawer.goto(x + btn_w, y)
    drawer.goto(x + btn_w, y - btn_h)
    drawer.goto(x, y - btn_h)
    drawer.goto(x, y)

    margin = int(btn_w * 0.3)

    drawer.penup()
    drawer.goto(x + margin, y - margin)
    drawer.pendown()
    drawer.goto(x + btn_w - margin, y - btn_h + margin)

    drawer.penup()
    drawer.goto(x + btn_w - margin, y - margin)
    drawer.pendown()
    drawer.goto(x + margin, y - btn_h + margin)





def callback(self, context):
    context['board'] = init(context['disk_number'])
    context['history'] = []
    context['animating'] = None
    context['dragging'] = None
    context['page'] = 'main_menu'


def hovers(self, mouse_x, mouse_y):
    mouse_x -= int(self.context['window_width'] / 2)
    mouse_y = -mouse_y + int(self.context['window_height'] / 2)

    x, y = get_position(self.context)

    btn_w = 50
    btn_h = 50

    inx = x <= mouse_x <= (x + btn_w)
    iny = (y - btn_h) <= mouse_y <= y

    return inx and iny
    


FinishGameButton.draw = type_wrapper(FinishGameButton, draw)
FinishGameButton.callback = type_wrapper(FinishGameButton, callback)
FinishGameButton.hovers = type_wrapper(FinishGameButton, hovers)
