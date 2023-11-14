from src.operations import moveDisque



def add_movement_to_history(context, de , a):
    moveDisque(context['board'],de, a)
    context['history'].append([de, a])


def undo_last_movement(context):
    if context['history'] != None:
        de, a= context['history'].pop()
        moveDisque(context['board'], a, de)



def view_history(context):
    for i in range(len(context['history'])):
        print("De:",context['history'][0]," à:",context['history'][1])
