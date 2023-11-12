from .generic import create_type, type_wrapper
from src.operations import *
from src.init import verifVictoire, init

from src.utils import maximum, minimum
from src.config import *

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
    mouse_x, mouse_y = event.x, event.y

    mouse_x -= int(self.context['window_width'] / 2)
    mouse_y = -mouse_y + int(self.context['window_height'] / 2)

    for i in range(N):
        disks_on_a_tower = self.context['board'][i]
        x, y = towerBasePosition(self.context, i)

        index = 0
        for disk in disks_on_a_tower:
            disk_width = getDiskWidth(self.context, disk)
            disk_x = x - int(disk_width / 2)
            disk_y = y + DISK_HEIGHT * index + int(DISK_HEIGHT / 2)
            disk_box = (disk_x, disk_y + int(DISK_HEIGHT / 2), disk_x + disk_width, disk_y - DISK_HEIGHT)

            is_hovered = mouse_hovers_this_disk(self.context, disk_box)

            if is_hovered:
                inner_x = mouse_x - disk_box[0]
                inner_y = mouse_y - disk_box[1]
                # print(inner_x, inner_y)

                self.context['dragging'] = [disk, (inner_x, inner_y)]

                # print(x, y)

                break

            index += 1



def on_mouse_release(self, event):
    dragged = self.context['dragging']
    if dragged:
        mouse_x, mouse_y = event.x, event.y
        mx = mouse_x - self.context['window_width'] / 2
        my = -mouse_y + self.context['window_height'] / 2
        
        tower = disk_is_in_a_towers_space(self.context)

        if tower != None:
            pos = posDisque(self.context['board'], dragged[0]) 
            if pos[0] != tower:
                moveDisque(self.context['board'], pos[0], tower)

                victory = verifVictoire(self.context['board'], N)
                
                if victory:
                    print('Its victory!!!!')
                    self.context['board'] = init(self.context['disk_number'])

        
        self.context['dragging'] = None
    



EventManager.on_mouse_move = type_wrapper(EventManager, on_mouse_move)
EventManager.on_mouse_click = type_wrapper(EventManager, on_mouse_click)
EventManager.on_mouse_release = type_wrapper(EventManager, on_mouse_release)