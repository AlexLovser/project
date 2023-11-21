from src.operations import moveDisque
from datetime import datetime


def add_movement_to_history(context, de , a):
    moveDisque(context['board'], de, a)
    context['history'].append([de, a])


def undo_last_movement(context):
    if context['history']:
        de, a = context['history'].pop()

        def on_finish():
            moveDisque(context['board'], a, de)

        context['animating'] = {
            'from_tower': a,
            'to_tower': de,
            'start_time': datetime.now(),
            'disk': context['board'][a][-1],
            'timeout': 400,
            'on_finish': on_finish
        }
        



def view_history(context):
    for i in range(len(context['history'])):
        print("De:", context['history'][0]," à:", context['history'][1])



def get_the_solution_instruction(context):
    to_move = [] 

    
    


    return to_move 
    


def show_the_solution(context, turtle):

    # to_move = []
    

    # for i in range(len(context['board'])):
    #     for j in context['board'][i]:
    #         to_move.append([i, 2])

    to_move = get_the_solution_instruction(context)
    n = 0

    def _show_the_solution():
        nonlocal n
        de, a = to_move[n]
        

        def on_finish():
            add_movement_to_history(context, de, a)

        context['animating'] = {
            'from_tower': de,
            'to_tower': a,
            'start_time': datetime.now(),
            'disk': context['board'][de][-1],
            'timeout': 600,
            'on_finish': on_finish
        }

        if n != len(to_move) - 1:
            turtle.screen.ontimer(_show_the_solution, t=1000)
        else:
            context['can_interact'] = True

        n += 1

    _show_the_solution()

    

    