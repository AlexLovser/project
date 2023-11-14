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

def renderUI(self, context):
    for i in self.ui.values():
        i.draw(self.turtle)


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

    self.renderUI(context)

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
RenderManager.renderUI = type_wrapper(RenderManager, renderUI)


