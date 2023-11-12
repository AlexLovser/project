
from copy import deepcopy

from src.init import *
from src.config import N
from src.operations import moveDisque

from src.cheating.types.render_manager import RenderManager
from src.cheating.types.event_manager import EventManager

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
    
    context = {
        "mouse_x": -200 + 3,
        "mouse_y": 100,
        "dragging": None,
        "mouse_x": 0,
    }

    RenderManager.is_interaction = True
    RenderManager.start_render(context)

    EventManager.context = context
    EventManager.window = RenderManager.window
    EventManager.window.getcanvas().bind("<Motion>", EventManager.on_mouse_move)


    RenderManager.window.mainloop()
        

    
if __name__ == '__main__':
    run()



