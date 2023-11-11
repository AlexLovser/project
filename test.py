
from copy import deepcopy

from src.init import *
from src.config import N
from src.operations import moveDisque

from src.cheating.types.render_manager import RenderManager
from src.cheating.types.event_manager import EventManager

import src.cheating.dictionary as Dict
from src.config import *



PLATEAU = init(N)
plateau = deepcopy(PLATEAU) # make a copy, not reference


# moveDisque(plateau, 0, 1)
# moveDisque(plateau, 0, 2)
# moveDisque(plateau, 0, 3)
# moveDisque(plateau, 0, 4)

# moveDisque(plateau, 1, 2)
# moveDisque(plateau, 4, 1)
# moveDisque(plateau, 0, 4)
# moveDisque(plateau, 1, 0)

# moveDisque(plateau, 0, 4)
# moveDisque(plateau, 3, 4)
# moveDisque(plateau, 2, 0)
# moveDisque(plateau, 2, 4)
# moveDisque(plateau, 0, 4)


# print(PLATEAU)
# print(plateau)
# print(verifVictoire(plateau, N))

def run():
    w = RenderManager.window.window_width()
    h = RenderManager.window.window_height()

    
    context = Dict.dictionary([
        ['mouse_x', 0], 
        ['mouse_y', 0],
        ['dragging', None],
        ['window_height', h],
        ['window_width', w],
    ])

    RenderManager.is_interaction = True
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



