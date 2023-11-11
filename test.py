import time

from src.cheating.types.render_manager import start_render, RenderManager

import src.cheating.dictionary as Dict
from src.config import *


RenderManager.is_interaction = True

def run():
    details = Dict.dictionary([
        ['x', -200 + 3], 
        ['y', 100]
    ])
    RenderManager.start_render(details)

    iteration = 0
    def start_iteraction():
        nonlocal iteration
        if iteration < 100:
            print("Process iteration #", iteration)
            Dict.setitem(details, 'x', -200 + 3 * iteration)
            iteration += 1
            RenderManager.window.ontimer(start_iteraction, t=30)

    start_iteraction()
    RenderManager.window.mainloop()
        

    
if __name__ == '__main__':
    run()

