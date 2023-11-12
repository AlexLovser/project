def maximum(array: list):
    m = array[0]

    for i in array:
        if i > m:
            m = i

    return m

def minimum(array: list):
    m = array[0]

    for i in array:
        if i < m:
            m = i

    return m


def bubbleSorting(array: list, order=1) -> None:
    for _ in range(len(array) + 1):
        for i in range(len(array) - 1):
            a = array[i]
            b = array[i + 1]

            if a > b:
                array[i], array[i + 1] = array[i + 1], array[i]

    if order == -1:
        array.reverse()


def loop_recursion_wrapper(func, ontimer_func, timeout, *args, **kwargs):
    def inner():
        func(*args, **kwargs)

        ontimer_func(func, t=timeout)

    return inner



