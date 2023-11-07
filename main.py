
from copy import deepcopy

from src.init import *
from src.config import N
from src.operations import moveDisque

PLATEAU = init(N)
plateau = deepcopy(PLATEAU) # make a copy, not reference


moveDisque(plateau, 0, 1)
moveDisque(plateau, 0, 2)
moveDisque(plateau, 0, 3)
moveDisque(plateau, 0, 4)

moveDisque(plateau, 1, 2)
moveDisque(plateau, 4, 1)
moveDisque(plateau, 0, 4)
moveDisque(plateau, 1, 0)

moveDisque(plateau, 0, 4)
moveDisque(plateau, 3, 4)
moveDisque(plateau, 2, 0)
moveDisque(plateau, 2, 4)
moveDisque(plateau, 0, 4)


print(PLATEAU)
print(plateau)
print(verifVictoire(plateau, N))


