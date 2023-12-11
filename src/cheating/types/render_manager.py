from src.cheating.types.generic import create_type, type_wrapper
from src.config import *
from src.operations import drawBoard, drawDisc, play_sound
import time
from src.init import init
from datetime import timedelta, datetime
import math
import random
from src.login import open_db, commit_db


import turtle as t

RenderManager = create_type('RenderManager')()
RenderManager.turtle = t.Turtle()
RenderManager.window = t.Screen()
RenderManager.turtle.hideturtle()

RenderManager.window.tracer(0, 0)
RenderManager.window.bgcolor("#222222")


def renderGameUI(self, context):
    elements = [self.ui['previous_button'], self.ui['solution_button'], self.ui['finishgame_button']]
    for i in elements:
        i.draw(self.turtle)

def renderMenuUI(self, context):
    elements = [self.ui['startgame_button']]
    for i in elements:
        i.draw(self.turtle)


def gameRender(self, context):
    self.turtle.pencolor(BOARD_COLOR)

    drawBoard(self.turtle, context)

    if context['is_victory']:
        context['is_interaction'] = False

        self.turtle.penup()
        self.turtle.goto(0, 150)
        self.turtle.pendown()

        time_spent = (datetime.now() - context['start_time']).total_seconds()
        profiles = open_db()

        avg_data = profiles[context['username']]['games']
        minutes, seconds = divmod(time_spent, 60)

        minutes = round(minutes)
        seconds = round(seconds)

        if avg_data:
            avg_time_spent = int(sum(i['time'] for i in avg_data) / len(avg_data))
            avg_minutes, avg_seconds = divmod(avg_time_spent, 60)
            avg_minutes = round(avg_minutes)
            avg_seconds = round(avg_seconds)
        else:
            avg_minutes = minutes
            avg_seconds = seconds
       


        ideal = 2 ** context['disk_number']  - 1
        score = len(context['history'])
        delta = score - ideal
        context['stats']['time'] = time_spent
        context['stats']['solution_used'] = context['solution_used']
        context['stats']['score'] = score
        context['stats']['ideal'] = ideal
        context['stats']['disk_number'] = context['disk_number']
        

        if context['solution_used']:
            context['stats']['win'] = False
            self.turtle.color("#00ffff")
            self.turtle.write("DEFEAT!!!", align="center", font=("ariel",48,"bold"))
            self.turtle.penup()
            self.turtle.goto(0, 100)
            self.turtle.pendown()
            self.turtle.write("You have used the soultion :(", align="center", font=("ariel",24,"bold"))
            profiles = open_db()
            time.sleep(5)
        else:
           
            if delta > ideal * 0.2:
                context['stats']['win'] = False
                self.turtle.color("#00ffff")
                self.turtle.write("DEFEAT!!!",align="center", font=("ariel",48,"bold"))
                self.turtle.penup()
                self.turtle.goto(0, 100)
                self.turtle.pendown()
                self.turtle.write(f"Too many moves: {len(context['history'])} / {int(ideal * 1.2)} [Ideal: {ideal}]", align="center", font=("ariel",24,"bold"))
                self.turtle.penup()
                self.turtle.goto(0, 130)
                self.turtle.pendown()
                self.turtle.write(f"Time spent: {minutes} min {seconds} sec / Average: {avg_minutes} min {avg_seconds} sec", align="center", font=("ariel",12,"bold"))
            else:
                play_sound('win')
                context['stats']['win'] = True
                self.turtle.color("#008000")
                self.turtle.write("VICTORY!!!",align="center", font=("ariel",48,"bold"))
                self.turtle.penup()
                self.turtle.goto(0, 100)
                self.turtle.pendown()
                self.turtle.write(f"Your moves {len(context['history'])} / {int(ideal * 1.2)} [Ideal: {ideal}]", align="center", font=("ariel",24,"bold"))
                self.turtle.penup()
                self.turtle.goto(0, 130)
                self.turtle.pendown()
                self.turtle.write(f"Time spent: {minutes} min {seconds} sec / Average: {avg_minutes} min {avg_seconds} sec", align="center", font=("ariel",12,"bold"))
            time.sleep(10)

        profiles[context['username']]['games'].append(context['stats'])
        commit_db(profiles)


        context['is_interaction'] = True
        context['is_victory'] = False
        context['solution_used'] = False
        context['board'] = init(context['disk_number'])
        context['start_time'] = datetime.now()
        context['history'] = []

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


def start_generating_stars(self, context):

    def inner():
        if context['page'] == 'main_menu':
            k = random.randint(-20, -2) / 4
            l = random.randint(40, 140)
            ww = int(context['window_width'] / 2)
            x = random.randint(-ww, ww )
            star_timeout = random.randint(1500, 3000)

            context['stars'].append([x, k, l, datetime.now(), star_timeout])
            t = random.randint(300, 700)
        else:
            t = 2000
        self.window.ontimer(inner, t=t)
    inner()


def renderStars(self, context):
    self.turtle.color('#ffffff')
    C = context['window_height'] / 2
    # print(len(context['stars']))

    to_remove = []
    index = -1
    for start_x, k, length, start_time, timeout in context['stars']:
        index += 1
        now = datetime.now()
        finish = start_time + timedelta(milliseconds=timeout)
        
        if now > finish:

            to_remove.append(index)
            continue

        delta = (now - start_time).total_seconds() * 1000 + 500

        half_width = context['window_width'] / 2

        j = int(start_x + (half_width - start_x) * (delta / timeout))
        i = int(k * j + C)

        b = int(length * math.sin(math.atan(k)))
        a = int((length ** 2 - b ** 2) ** 0.5)
        
        end_point = [j + a, i + b]

        colors = ['#94c9e4', '#afddec', '#d0e3ed']
        for iteration in range(3):
            new_start_x = start_x + (iteration * a * 0.5)
            x = int(new_start_x + (half_width - new_start_x) * (delta / timeout))
            y = int(k * x + C)
            self.turtle.color(colors[iteration])
            self.turtle.pensize(1 + int(1.5 * iteration))
            self.turtle.penup()
            self.turtle.goto((x, y))
            self.turtle.pendown()
            self.turtle.goto(end_point)


    context['stars'] = [item for index, item in enumerate(context['stars']) if index not in to_remove]

       
def mainMenuRender(self, context):
    self.renderStars(context)
    self.renderMenuUI(context)

def render(self, context):
    if context['page'] == 'game':
        self.gameRender(context)
    elif context['page'] == 'main_menu':
        self.mainMenuRender(context)


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
RenderManager.renderMenuUI = type_wrapper(RenderManager, renderMenuUI)
RenderManager.mainMenuRender = type_wrapper(RenderManager, mainMenuRender)
RenderManager.renderStars = type_wrapper(RenderManager, renderStars)
RenderManager.gameRender = type_wrapper(RenderManager, gameRender)
RenderManager.start_generating_stars = type_wrapper(RenderManager, start_generating_stars)


