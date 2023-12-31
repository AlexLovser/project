from src.init import *
from src.config import N

from src.cheating.types.render_manager import RenderManager
from src.cheating.types.event_manager import EventManager

from src.config import *
from src.operations import *

from src.cheating.types.ui.previous_tour_btn import PreviousButton
from src.cheating.types.ui.solution_btn import SolutionButton
from src.cheating.types.ui.start_game_btn import StartGameButton
from src.cheating.types.ui.finish_game_btn import FinishGameButton


from src.login import auth, open_db, commit_db, get_diificulty


def run():
    context = {
        'is_interaction': True,
        "mouse_x": 0,
        "mouse_y": 0,
        "dragging": None,
        'animating': None,
        "window_width": RenderManager.window.window_width(),
        "window_height": RenderManager.window.window_height(),
        'disk_number': N + 0 , # or more
        'disk_colors': {},
        'disk_colors_adjusted': {},
        'is_victory': False,
        'history': [],
        'page': 'main_menu',
        'can_interact': True,
        'solution_used': False,
        'stars': [],
        'stats': {}
    }

    UI = {
        'previous_button': PreviousButton,
        'solution_button': SolutionButton,
        'startgame_button': StartGameButton,
        'finishgame_button': FinishGameButton,
    }

    credentials = auth()

    if credentials is None:
        return
    
    username = credentials
    # username = 'alexlovser'
    context['username'] = username
    

    D = get_diificulty()
    context['disk_number'] = 3 + D
    play_sound('click')


    for i in UI.values():
        i.context = context
        i.turtle = RenderManager.turtle


    context['board'] = init(context['disk_number'])

    for i in range(context['disk_number']):
        context['disk_colors'][i + 1] = generateDiskColor(context, i + 1)
        context['disk_colors_adjusted'][i + 1] = adjust_color_lighten(*hex_to_rgb(context['disk_colors'][i + 1]), 0.4)


    

    

    RenderManager.ui = UI
    RenderManager.start_render(context)
    RenderManager.start_generating_stars(context)
    RenderManager.window.title(f"Hanoi Towers | {username}")

    EventManager.ui = UI
    EventManager.context = context
    EventManager.window = RenderManager.window
    

    bind = EventManager.window.getcanvas().bind
    bind("<Motion>", EventManager.on_mouse_move)
    bind("<Button-1>", EventManager.on_mouse_click)
    bind("<ButtonRelease-1>", EventManager.on_mouse_release)


    RenderManager.window.mainloop()
        

    
if __name__ == '__main__':
    run()



