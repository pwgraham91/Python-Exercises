__author__ = 'petergraham'


def fibonacci():
    fib_list = [0, 1]
    counter = 0
    while counter < 100:
        a = fib_list[-1]
        b = fib_list[-2]
        fib_list.append(a + b)
        counter += 1
    print fib_list

fibonacci()