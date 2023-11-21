from src.operations import moveDisque
from datetime import datetime
from src.init import init, verifVictoire



def add_movement_to_history(context, de , a):
    moveDisque(context['board'], de, a)
    context['history'].append([de, a])

    if verifVictoire(context['board'], context['disk_number']):
        context['is_victory'] = True


def undo_last_movement(context):
    if context['history'] and context['can_interact']:
        de, a = context['history'].pop()
        context['can_interact'] = False

        def on_finish():
            moveDisque(context['board'], a, de)
            context['can_interact'] = True

        context['animating'] = {
            'from_tower': a,
            'to_tower': de,
            'start_time': datetime.now(),
            'disk': context['board'][a][-1],
            'timeout': 400,
            'on_finish': on_finish
        }
        

def get_the_solution_instruction(context):
    to_move = []

    def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
        if n == 0: 
            return 
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
        to_move.append([from_rod,to_rod])
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 

    TowerOfHanoi(context['disk_number'],0,2,1) 
    return to_move

def show_the_solution(context, turtle):

    context['board'] = init(context['disk_number'])
    to_move = get_the_solution_instruction(context)
    n = 0

    def _show_the_solution():
        nonlocal n
        de, a = to_move[n]
        
        context['can_interact'] = False

        def on_finish():
            add_movement_to_history(context, de, a)

        context['animating'] = {
            'from_tower': de,
            'to_tower': a,
            'start_time': datetime.now(),
            'disk': context['board'][de][-1],
            'timeout': 700,
            'on_finish': on_finish
        }

        if n != len(to_move) - 1:
            n += 1
            turtle.screen.ontimer(_show_the_solution, t=context['animating']['timeout'] + 50)
        else:
            context['can_interact'] = True

        

    _show_the_solution()

    

    