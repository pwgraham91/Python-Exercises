from typing import List
from random import randrange


def do_shuffle(_list: List[int]):
    length = len(_list)
    current_spot = 0

    for i in range(length):
        random_swap_index = randrange(current_spot, length)
        _list[current_spot], _list[random_swap_index] = _list[random_swap_index], _list[current_spot]
        current_spot += 1

    return _list

my_range = list(range(5))
print(my_range)

print(do_shuffle(my_range))
