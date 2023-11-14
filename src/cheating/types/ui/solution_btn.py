from src.cheating.types.generic import create_type, type_wrapper
from src.history import show_the_solution


SolutionButton = create_type('SolutionButton')()


def get_position(ctx):
    W = ctx['window_width']
    H = ctx['window_height']
    x = int(W / 2) - 175
    y = int(H / 2) - 100

    return x, y


def draw(self, drawer):
    x, y = get_position(self.context)

    is_hovered = self.hovers(self.context['mouse_x'], self.context['mouse_y'])

    drawer.penup()
    drawer.color('yellow')
    drawer.pensize(3 + 5 * is_hovered)
    drawer.goto(x, y)
    drawer.pendown()

    btn_w = 30
    btn_h = 30
    drawer.circle(btn_w)

    y += 35
    x -= 7

    drawer.penup()
    drawer.pensize(2 + 5 * is_hovered)
    drawer.goto(x, y)
    drawer.pendown()

    drawer.goto(x, y + 10)
    drawer.goto(x + 15, y + 10)
    drawer.goto(x + 15, y - 10)
    drawer.goto(x + 7, y - 10)
    drawer.goto(x + 7, y - 20)

    drawer.penup()
    drawer.goto(x + 7, y - 25)
    drawer.pendown()
    drawer.pensize(4 + 5 * is_hovered)
    drawer.goto(x + 7, y - 26)
   

def callback(self, context):
    context['can_interact'] = False

    show_the_solution(context, self.turtle)

    


def hovers(self, mouse_x, mouse_y):
    mouse_x -= int(self.context['window_width'] / 2)
    mouse_y = -mouse_y + int(self.context['window_height'] / 2)

    x, y = get_position(self.context)

    btn_w = 30
    btn_h = 30

    inx = (x - btn_w) <= mouse_x <= (x + btn_w)
    iny = (y - btn_h) <= mouse_y <= (y + btn_h * 2)

    return inx and iny


SolutionButton.draw = type_wrapper(SolutionButton, draw)
SolutionButton.callback = type_wrapper(SolutionButton, callback)
SolutionButton.hovers = type_wrapper(SolutionButton, hovers)
