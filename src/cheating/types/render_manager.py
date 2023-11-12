from src.cheating.types.generic import create_type, type_wrapper
from src.config import *
from src.operations import drawBoard, drawDisc


import turtle as t

RenderManager = create_type('RenderManager')()
RenderManager.turtle = t.Turtle()
RenderManager.window = t.Screen()
RenderManager.turtle.hideturtle()

RenderManager.window.tracer(0, 0)
RenderManager.window.bgcolor("white")
RenderManager.window.title("Hanoi Towers")


def square(drawer: t.Turtle):
    drawer.pendown()
    for _ in range(2):
        drawer.forward(50)
        drawer.left(90)
        drawer.forward(50)
        drawer.left(90)


def filled_square(drawer: t.Turtle):
    drawer.pensize(50)
    # drawer.shape("square")
    drawer.left(90)
    drawer.forward(25)
    drawer.right(90)
    drawer.pendown()
    drawer.forward(50)
    

def render(self, context):
    # self.turtle.penup()
    # mouse_x = obj_position['mouse_x']
    # mouse_y = obj_position['mouse_y']
    # wh = obj_position['window_height']
    # ww = obj_position['window_width']
    # self.turtle.goto(int(mouse_x - ww / 2), int(-mouse_y + wh / 2))
    # filled_square(self.turtle)

    drawBoard(self.turtle, context)

    for i in range(context['disk_number']):
        color = context['disk_colors'][i + 1]
        drawDisc(self.turtle, context, i + 1, context['board'], color)

    self.turtle.pencolor('#000')


def start_render(self, *args, **kwargs):
    delayms =int(round(FRAME_DELAY * 1000))
    def inner():
        if self.is_interaction:
            self.turtle.clear() # removing all previous traces
            self.render_function(*args, **kwargs)
            self.window.update() # updating to show the picture
        self.window.ontimer(inner, t=delayms)

    inner()



RenderManager.render_function = type_wrapper(RenderManager, render)
RenderManager.start_render = type_wrapper(RenderManager, start_render)

