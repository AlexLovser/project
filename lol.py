from turtle import Turtle, mainloop
from src.config import *
from src.operations import drawBoard, generateDiskColor, drawDisc
from src.init import *

turtle = Turtle()
turtle.speed(0)

context = {
    'window_width': turtle.screen.window_width(),
    'window_height': turtle.screen.window_height(),
    'disk_number': 10, # or more
    'disk_colors': {}
}

for i in range(context['disk_number']):
    context['disk_colors'][i + 1] = generateDiskColor(context, i + 1)

drawBoard(turtle, context)



PLATEAU = init(context['disk_number'])

for i in range(context['disk_number']):
    color = context['disk_colors'][i + 1]
    drawDisc(turtle, context, i + 1, PLATEAU, color)




mainloop()