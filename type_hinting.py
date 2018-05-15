import typing


def fun(a='b') -> int:
    return a


def string(a: str):
    return a


def fun_b(a: typing.Union[str, int]):
    return a


print(fun_b('s'))
print(fun_b(1))
print(fun_b([1]))
print(fun(None))

