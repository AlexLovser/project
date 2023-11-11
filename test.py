import time

from src.cheating.types.render_manager import RenderManger

import src.cheating.dictionary as Dict
from src.config import *


RenderManger.is_interaction = True


def run():
    details = Dict.dictionary([
        ['x', -200 + 3], 
        ['y', 100]
    ])
    RenderManger.start_render(details)

    for iteration in range(100):
        time.sleep(0.5)
        print("Process iteration #", iteration)
        Dict.setitem(details, 'x', -200 + 3 * iteration)

    RenderManger.window.mainloop()
        

    
if __name__ == '__main__':
    run()

