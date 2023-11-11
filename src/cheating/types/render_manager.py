from src.cheating.types.generic import create_type, type_wrapper
from src.config import FRAME_DELAY
import src.cheating.dictionary as Dict

import turtle as t

RenderManager = create_type('RenderManager')()
RenderManager.turtle = t.Turtle()
RenderManager.window = t.Screen()

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
    

def render(self, obj_position):
    self.turtle.penup()
    self.turtle.goto(Dict.values(obj_position))
    filled_square(self.turtle)


def start_render(self, *args, **kwargs):
    def inner():
        if self.is_interaction:
            self.turtle.clear() # removing all previous traces
            self.render_function(*args, **kwargs)
            self.window.update() # updating to show the picture
        self.window.ontimer(inner, t=int(round(FRAME_DELAY * 1000)))

    inner()



RenderManager.render_function = type_wrapper(RenderManager, render)
RenderManager.start_render = type_wrapper(RenderManager, start_render)
