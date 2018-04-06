__author__ = 'petergraham'


def median(data):
    data.sort()
    if len(data) % 2 == 0:
        under = data[int(((len(data) - 1) / 2.0) - .5)]
        over = data[int(((len(data) - 1) / 2.0) + .5)]
        return (under + over) / 2.0
    else:
        return data[len(data) / 2]


print median([3, 6, 20, 99, 10, 15])