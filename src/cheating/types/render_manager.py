from src.cheating.types.generic import create_type, type_wrapper
from src.config import FRAME_DELAY

from time import sleep
import turtle as t
from threading import Thread

turtle = t.Turtle()



RenderManger = create_type('RenderManger')()
RenderManger.turtle = t.Turtle()
RenderManger.window = t.Screen()

RenderManger.window.tracer(0, 0)
RenderManger.window.bgcolor("white")
RenderManger.window.title("Hanoi Towers")


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
    self.turtle.goto(obj_position)
    filled_square(self.turtle)


def start_render(self, *args, **kwargs):
    def inner(*args, **kwargs):
        while True:
            if self.is_interaction:
                sleep(FRAME_DELAY)
                self.turtle.clear() # removing all previous traces
                self.render_function(*args, **kwargs)
                self.window.update() # updating to show the picture
        
        
        
    Thread(name='Render()', target=inner, args=args, kwargs=kwargs).start() # independent process of rendering



RenderManger.render_function = type_wrapper(RenderManger, render)
RenderManger.start_render = type_wrapper(RenderManger, start_render)
