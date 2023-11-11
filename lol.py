import turtle
import random

# global colors 
col = ['red', 'yellow', 'green', 'blue',
       'white', 'black', 'orange', 'pink']


# method to call on timer


# set screen 
sc = turtle.Screen()
sc.setup(400, 300)

def fxn():
    global col
    ind = random.randint(0, 7)

    # set background color of the
    # turtle screen randomly
    sc.bgcolor(col[ind])
    sc.ontimer(fxn, 500)


sc.mainloop()
fxn()