# render_manager.py

import turtle
import threading

class RenderManager:
    def __init__(self):
        self.draw_function = None

    def set_draw_function(self, draw_function):
        self.draw_function = draw_function

    def start_rendering(self):
        turtle.onscreenclick(self._on_click)
        turtle.mainloop()

    def _on_click(self, x, y):
        if self.draw_function:
            # Вызываем функцию отрисовки в главном потоке
            turtle.bye()
            self.draw_function(x, y)

# main_script.py


def draw_function(x, y):
    print(f"Drawing at coordinates ({x}, {y})")

if __name__ == "__main__":
    manager = RenderManager()
    manager.set_draw_function(draw_function)

    render_thread = threading.Thread(target=manager.start_rendering)
    render_thread.start()

    render_thread.join()
