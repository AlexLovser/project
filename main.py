from src.init import *
from src.config import N

from src.cheating.types.render_manager import RenderManager
from src.cheating.types.event_manager import EventManager

from src.config import *
from src.operations import *


def run():
    context = {
        'is_interaction': True,
        "mouse_x": 0,
        "mouse_y": 0,
        "dragging": None,
        "window_width": RenderManager.window.window_width(),
        "window_height": RenderManager.window.window_height(),
        'disk_number': N + 2 , # or more
        'disk_colors': {},
        'disk_colors_adjusted': {},
        'is_victory': False
        
    }

    context['board'] = init(context['disk_number'])

    for i in range(context['disk_number']):
        context['disk_colors'][i + 1] = generateDiskColor(context, i + 1)
        context['disk_colors_adjusted'][i + 1] = adjust_color_lighten(*hex_to_rgb(context['disk_colors'][i + 1]), 0.4)


    RenderManager.start_render(context)

    EventManager.context = context
    EventManager.window = RenderManager.window

    bind = EventManager.window.getcanvas().bind
    bind("<Motion>", EventManager.on_mouse_move)
    bind("<Button-1>", EventManager.on_mouse_click)
    bind("<ButtonRelease-1>", EventManager.on_mouse_release)


    RenderManager.window.mainloop()
        

    
if __name__ == '__main__':
    run()



