"""
https://www.hackerrank.com/challenges/frequency-queries/problem
"""


def add_to_value_dict(value_dict, key_dict, integer):
    if value_dict.get(key_dict[integer]):
        value_dict[key_dict[integer]].add(integer)
    else:
        value_dict[key_dict[integer]] = {integer}


def subtract_from_value_dict(value_dict, key_dict, integer):
    try:
        value_dict[key_dict[integer]].remove(integer)
    except ValueError as e:
        pass


def freq_query(queries):
    output = []
    key_dict = {}
    value_dict = {}
    for command, integer in queries:
        if command == 1:
            if key_dict.get(integer):
                subtract_from_value_dict(value_dict, key_dict, integer)
                key_dict[integer] += 1
                add_to_value_dict(value_dict, key_dict, integer)
            else:
                key_dict[integer] = 1
                add_to_value_dict(value_dict, key_dict, integer)
        elif command == 2:
            if key_dict.get(integer):
                subtract_from_value_dict(value_dict, key_dict, integer)
                key_dict[integer] -= 1
                add_to_value_dict(value_dict, key_dict, integer)
        else:
            if value_dict.get(integer):
                output.append(1)
            else:
                output.append(0)
    return output



assert freq_query([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]) == [0, 1]
