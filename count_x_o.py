"""
    Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
    insensitive. The string can contain any other characters as well. You are only concerned with whether it has the
    same number of Xs and Os.
"""


def count_xo(string):
    count_x = 0
    count_o = 0

    for i in string:
        if i in ['X', 'x']:
            count_x += 1
        elif i in ['O', 'o']:
            count_o += 1

    return count_x == count_o


assert count_xo('ooxx')
assert not count_xo('xooxx')
assert count_xo('ooxXm')
assert count_xo('zpzpzpp')
assert not count_xo('zzoo')
