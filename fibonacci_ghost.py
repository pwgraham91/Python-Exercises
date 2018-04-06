__author__ = 'petergraham'


def fibonacci_ghost(opacity):
    fib_list = [0, 1]
    ghost_opacity = [10000]
    for i in range(30):
        a = fib_list[-1]
        b = fib_list[-2]
        c = a + b
        fib_list.append(c)
    fib_list.pop(1)
    counter = 0
    while ghost_opacity[-1] > 0:
        counter += 1
        if counter in fib_list:
            ghost_opacity.append(ghost_opacity[-1] - counter)
        else:
            ghost_opacity.append(ghost_opacity[-1] + 1)
    return ghost_opacity.index(opacity)

print fibonacci_ghost(9995)
