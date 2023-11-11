def on_mouse_move( x , y):
    
    w = 1000
    h = 2000

    x = max((0, x))
    x = min((w, x))

    y = max((0, y))
    y = min((h, y))

    print(x, y)

on_mouse_move(1001, 10000)

