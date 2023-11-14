from src.operations import moveDisque



def add_movement_to_history(context, de , a):
    moveDisque(context['board'], de, a)
    context['history'].append([de, a])


def undo_last_movement(context):
    if context['history']:
        de, a = context['history'].pop()
        moveDisque(context['board'], a, de)



def view_history(context):
    for i in range(len(context['history'])):
        print("De:", context['history'][0]," à:", context['history'][1])



def show_the_solution(context, turtle):
    # temporary interpretation

    to_move = []
    


    for i in range(len(context['board'])):
        for j in context['board'][i]:
            to_move.append([i, 2])


    print(to_move)
    n = 0

    def _show_the_solution():
        nonlocal n
        add_movement_to_history(context, *to_move[n])

        if n != len(to_move) - 1:
            turtle.screen.ontimer(_show_the_solution, t=1000)
        else:
            print('ttt')
            context['can_interact'] = True

        n += 1

    _show_the_solution()

    

    