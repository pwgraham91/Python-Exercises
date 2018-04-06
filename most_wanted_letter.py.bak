__author__ = 'petergraham'


def most_wanted_letter(text):
    string = text.lower()
    dictionary = [
        ['a', 0],
        ['b', 0],
        ['c', 0],
        ['d', 0],
        ['e', 0],
        ['f', 0],
        ['g', 0],
        ['h', 0],
        ['i', 0],
        ['j', 0],
        ['k', 0],
        ['l', 0],
        ['m', 0],
        ['n', 0],
        ['o', 0],
        ['p', 0],
        ['q', 0],
        ['r', 0],
        ['s', 0],
        ['t', 0],
        ['u', 0],
        ['v', 0],
        ['w', 0],
        ['x', 0],
        ['y', 0],
        ['z', 0],
    ]
    for i in string:
        if i.isalpha():
            counter = 0
            for a in dictionary:
                if i == dictionary[counter][0]:
                    dictionary[counter][1] += 1
                counter += 1
    max_letters = 0
    for i in dictionary:
        if max_letters < i[1]:
            max_letters = i[1]
    max_list = []
    for i in dictionary:
        if max_letters == i[1]:
            max_list.append(i[0])
    return max_list[0]


print most_wanted_letter("Hello World")
