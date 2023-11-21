from src.cheating.types.generic import create_type, type_wrapper
from src.config import *
from src.operations import drawBoard, drawDisc
import time
from src.init import init
from datetime import timedelta, datetime


import turtle as t

RenderManager = create_type('RenderManager')()
RenderManager.turtle = t.Turtle()
RenderManager.window = t.Screen()
RenderManager.turtle.hideturtle()

RenderManager.window.tracer(0, 0)
RenderManager.window.bgcolor("#222222")
RenderManager.window.title("Hanoi Towers")

def renderGameUI(self, context):
    for i in self.ui.values():
        i.draw(self.turtle)


def gameRender(self, context):
    self.turtle.pencolor(BOARD_COLOR)

    drawBoard(self.turtle, context)

    if context['is_victory']:
        context['is_interaction'] = False

        self.turtle.penup()
        self.turtle.goto(0, 150)
        self.turtle.pendown()


        if context['solution_used']:
            self.turtle.color("#00ffff")
            self.turtle.write("DEFEAT!!!", align="center", font=("ariel",48,"bold"))
            self.turtle.penup()
            self.turtle.goto(0, 100)
            self.turtle.pendown()
            self.turtle.write("You have used the soultion :(", align="center", font=("ariel",24,"bold"))

        else:
            ideal = 2 ** context['disk_number'] - 1
            delta = len(context['history'])  - ideal
            if delta > ideal * 0.2:
                self.turtle.color("#00ffff")
                self.turtle.write("DEFEAT!!!",align="center", font=("ariel",48,"bold"))
                self.turtle.penup()
                self.turtle.goto(0, 100)
                self.turtle.pendown()
                self.turtle.write(f"Too many moves: {len(context['history'])} / {int(ideal * 1.2)} [Ideal: {ideal}]", align="center", font=("ariel",24,"bold"))
            else:
                self.turtle.color("#008000")
                self.turtle.write("VICTORY!!!",align="center", font=("ariel",48,"bold"))
                self.turtle.penup()
                self.turtle.goto(0, 100)
                self.turtle.pendown()
                self.turtle.write(f"Your moves {len(context['history'])} / {int(ideal * 1.2)} [Ideal: {ideal}]", align="center", font=("ariel",24,"bold"))


        time.sleep(5)
        
        context['is_interaction'] = True
        context['is_victory'] = False
        context['board'] = init(context['disk_number'])

        return
    

    if context['animating']:
        end_time = context['animating']['start_time'] + timedelta(milliseconds=context['animating']['timeout'])
        if (end_time < datetime.now()):
            context['animating']['on_finish']()
            context['animating'] = None

    for i in range(context['disk_number']):
        drawDisc(self.turtle, context, i + 1, context['board'])

    self.renderGameUI(context)
    self.turtle.pencolor(BOARD_COLOR)


def render(self, context):
    if context['page'] == 'game':
        gameRender(self, context)


def start_render(self, *args, **kwargs):
    delayms = int(round(FRAME_DELAY * 1000))
    def inner():
        if args[0]['is_interaction']:
            self.turtle.clear() # removing all previous traces
            self.render_function(*args, **kwargs)
            self.window.update() # updating to show the picture
        self.window.ontimer(inner, t=delayms)

    inner()



RenderManager.render_function = type_wrapper(RenderManager, render)
RenderManager.start_render = type_wrapper(RenderManager, start_render)
RenderManager.renderGameUI = type_wrapper(RenderManager, renderGameUI)


