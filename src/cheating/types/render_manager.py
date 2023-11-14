from src.cheating.types.generic import create_type, type_wrapper
from src.config import *
from src.operations import drawBoard, drawDisc
import time


import turtle as t

RenderManager = create_type('RenderManager')()
RenderManager.turtle = t.Turtle()
RenderManager.window = t.Screen()
RenderManager.turtle.hideturtle()

RenderManager.window.tracer(0, 0)
RenderManager.window.bgcolor("#222222")
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
    self.turtle.pencolor(BOARD_COLOR)

    drawBoard(self.turtle, context)

    if context['is_victory']:
        context['is_interaction'] = False

        self.turtle.penup()
        self.turtle.goto(0, 150)
        self.turtle.pendown()
        self.turtle.color("#008000")
        self.turtle.write("VICTORY!!!",align="center", font=("ariel",48,"bold"))
        time.sleep(3)
        
        context['is_interaction'] = True
        context['is_victory'] = False

        return

    for i in range(context['disk_number']):
        drawDisc(self.turtle, context, i + 1, context['board'])

    self.turtle.pencolor(BOARD_COLOR)


def start_render(self, *args, **kwargs):
    delayms =int(round(FRAME_DELAY * 1000))
    def inner():
        if args[0]['is_interaction']:
            self.turtle.clear() # removing all previous traces
            self.render_function(*args, **kwargs)
            self.window.update() # updating to show the picture
        self.window.ontimer(inner, t=delayms)

    inner()



RenderManager.render_function = type_wrapper(RenderManager, render)
RenderManager.start_render = type_wrapper(RenderManager, start_render)

