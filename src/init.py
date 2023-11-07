def init(n): # n is number of discs and towers
    towers = []
    for i in range(n):
        towers.append([])
        towers[0].append(n-i)
    return towers
