def maximum(array):
    m = 0

    for i in array:
        if i > m:
            m = i

    return m
