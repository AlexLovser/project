from src.config import N
from src.history import add_movement_to_history



context = {
    'is_interaction': True,
    "mouse_x": 0,
    "mouse_y": 0,
    "dragging": None,
    'disk_number': N + 2 , # or more
    'disk_colors': {},
    'disk_colors_adjusted': {},
    'is_victory': False,
    'history': []
}


def find_the_solution(context, auxiliary):
    # movements = []


    # def hanoi_recursive(n, de, a, auxiliary):
    #     if n == 1:
    #         add_movement_to_history(context, de, a)
    #     else:
    #         hanoi_recursive(n-1, source, auxiliary, target)
    #         move_disk(n, source, target)
    #         hanoi_recursive(n-1, auxiliary, target, source)

    # hanoi_recursive(context['disk_number'], source, target, auxiliary)
    # return movements


movements = find_the_solution(context)

print(movements)


