"""
1 2 3 4 5
person 3 bribes 2 to move up
1 3 2 4 5

no person can afford to bribe more than 2 times (too chaotic)
what is the minimum number of bribes to get to this state
"""
from operator import itemgetter


class Breaker(Exception):
    pass

unparsed = '2 1 5 3 4'
q = map(int, unparsed.split())


def spots_away_from_initial(arr):
    spots_away = []
    for index, element in enumerate(arr):
        spots_away.append([element, element - index, index])

    return sorted(spots_away, key=itemgetter(1), reverse=True)


def flip_spots(n):
    big_mover = spots_arr[n][0]
    spots_away = spots_arr[n][1]
    position = spots_arr[n][2]

    if spots_away == 1:
        print i
        raise Breaker('all done')
    up_or_down = 1 if spots_away > 0 else -1
    totem_pole = q[position] > q[position + up_or_down]
    if up_or_down == 1:
        if not totem_pole:
            flip_spots(n + 1)
            return
        briber = bribe_book.get(big_mover)
        if not briber:
            bribe_book[big_mover] = 1
        else:
            bribe_book[big_mover] += 1
    else:
        if totem_pole:
            flip_spots(n + 1)
            return
    q[position], q[position + up_or_down] = q[position + up_or_down], q[position]


bribe_book = {}

try:
    while True:
        spots_arr = spots_away_from_initial(q)
        for value in bribe_book.values():
            if value > 2:
                print 'Too chaotic'
                raise Breaker('all done')
        flip_spots(0)
    else:
        print 'finished'
except Breaker as e:
    if e.message != 'all done':
        raise e

