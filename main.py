# from turtle import Turtle
from copy import deepcopy

from src.init import *
from src.config import N

# turtle = Turtle()
PLATEAU = init(N)

print(PLATEAU)
# print(nbDisques(PLATEAU, 0))
# print(disqueSup(PLATEAU, 0))
# print(posDisque(PLATEAU, 4))



plateau = deepcopy(PLATEAU)




def moveDisque(P, de, a):
    plateau[a].append(plateau[de].pop())


moveDisque(plateau, 0, 4)
print(plateau)
print(verifDepl(PLATEAU, PLATEAU, plateau))



