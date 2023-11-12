from src.utils import bubbleSorting


def init(n): # n is number of discs and towers
    towers = [[], [], []]
    for i in range(n):
        towers[0].append(n-i)
    return towers


def nbDisques(P, x):
    return len(P[x])


def disqueSup(P, x):
    y = P[x]
    if y:
        return max(y)
    return -1


def posDisque(P, d):
    for i in range(len(P)):
        _X = P[i] # tower
        for x in range(len(_X)):
            if _X[x] == d:
                return i, x
        

def verifDepl(P, p1, p2):
    if len(p1) == len(p2):
        for i in range(len(P)):
            a = p1[i]
            b = p2[i]

            if a != b:
                if abs(len(a) - len(b)) <= 1:
                    return True
                
    return False


def verifVictoire(P, n):
    gauches = P[:-1]

    if any(gauches):
        return False
    
    to_sort = P[-1].copy()
    bubbleSorting(to_sort, -1)

    return to_sort == P[-1]
