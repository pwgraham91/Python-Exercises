from functools import partial

from infix import shift_infix


class Infix:
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        a = partial(self.func, other)
        return Infix(a)

    def __call__(self, v1, v2):
        return self.func(v1, v2)


@Infix
def add(x, y):
    return x + y


a = 1 | add
b = a | 2
print(b)
print(5 | add | 6)


@shift_infix
def plus(a, b):
    return a + b


print(3 << plus >> 4)
