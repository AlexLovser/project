from .generic import create_type, type_wrapper


from src.utils import maximum, minimum
from src.config import WINDOW_MARGIN

EventManager = create_type('EventManager')()


def on_mouse_move(self, event):
    x, y = event.x, event.y
    
    w = self.window.window_width()
    h = self.window.window_height()

    x = maximum((WINDOW_MARGIN, x))
    x = minimum((w - WINDOW_MARGIN, x))

    y = maximum((WINDOW_MARGIN, y))
    y = minimum((h - WINDOW_MARGIN, y))
    
    self.context['window_width'] = w
    self.context['window_height'] = h
    self.context['mouse_x'] = int(x)
    self.context['mouse_y'] = int(y)


def on_mouse_click(self, event):
    x, y = event.x, event.y
    print('Clicked!', x, y)


def on_mouse_release(self, event):
    x, y = event.x, event.y
    print('Released!', x, y)


EventManager.on_mouse_move = type_wrapper(EventManager, on_mouse_move)
EventManager.on_mouse_click = type_wrapper(EventManager, on_mouse_click)
EventManager.on_mouse_release = type_wrapper(EventManager, on_mouse_release)