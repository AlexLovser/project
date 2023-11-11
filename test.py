import time

from src.cheating.types.render_manager import RenderManager

import src.cheating.dictionary as Dict
from src.config import *


RenderManager.is_interaction = True

def run():
    details = Dict.dictionary([
        ['x', -200 + 3], 
        ['y', 100]
    ])
    RenderManager.start_render(details)

    # iteration = 0
    # def start_iteraction():
    #     nonlocal iteration
    #     if iteration < 1000:
    #         # print("Process iteration #", iteration)
    #         Dict.setitem(details, 'x', -300 + 3 * iteration)
    #         iteration += 1
    #         RenderManager.window.ontimer(start_iteraction, t=30)

    # start_iteraction()

    def print_mouse_position(event):
        x, y = event.x, event.y
        w = RenderManager.window.window_width()
        h = RenderManager.window.window_height()
        Dict.setitem(details, 'x', x - int(w / 2))
        Dict.setitem(details, 'y', -y + int(h / 2))
        # print(f"Mouse position: x = {x}, y = {y}")

    RenderManager.window.getcanvas().bind("<Motion>", print_mouse_position)


    RenderManager.window.mainloop()
        

    
if __name__ == '__main__':
    run()

