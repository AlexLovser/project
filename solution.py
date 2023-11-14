from src.config import N

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

def hanoi(n, source, target, auxiliary):
    movements = []

    def move_disk(disk, source, target):
        movements.append((disk, "de", source, "à",target))

    def hanoi_recursive(n, source, target, auxiliary):
        if n == 1:
            move_disk(1, source, target)
        else:
            hanoi_recursive(n-1, source, auxiliary, target)
            move_disk(n, source, target)
            hanoi_recursive(n-1, auxiliary, target, source)

    hanoi_recursive(n, source, target, auxiliary)
    return movements

movements = hanoi(context['disk_number'], "1er", "2nd", "3th")
print(movements)
