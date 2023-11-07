from src.utils import maximum


def init(n): # n is number of discs and towers
    towers = []
    for i in range(n):
        towers.append([])
        towers[0].append(n-i)

    return towers


def nbDisques(P, x):
    return len(P[x])


def disqueSup(P, x):
    y = P[x]
    if y:
        return maximum(y)
    return -1


def posDisque(P, d):
    for i in range(len(P)):
        x = P[i]
        if d in x:
            return i
        

def verifDepl(P, p1, p2):
    if len(p1) == len(p2):
        for i in range(len(P)):
            a = p1[i]
            b = p2[i]

            if a != b:
                if abs(len(a) - len(b)) <= 1:
                    return True
                
    return False


        
    
