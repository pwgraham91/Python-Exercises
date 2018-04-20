"""
Create a function that takes a list of non-negative integers and strings and returns a new list with the strings 
filtered out.
"""


def filter_list(array):
    return list(filter(lambda x: type(x) == int, array))


def filter_list_comprehension(array):
    return [x for x in array if type(x) == int]

import datetime

start = datetime.datetime.now()

assert filter_list_comprehension([1, 2, 'a', 'b']) == [1, 2]
assert filter_list_comprehension([1, 'a', 'b', 0, 15]) == [1, 0, 15]
assert filter_list_comprehension([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]

stop = datetime.datetime.now()
print(stop - start)


start = datetime.datetime.now()

assert filter_list([1, 2, 'a', 'b']) == [1, 2]
assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]

stop = datetime.datetime.now()
print(stop - start)
