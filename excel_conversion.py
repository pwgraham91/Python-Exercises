"""
Microsoft Excel numbers cells as 1...26 and after that AA, AB.... AAA, AAB...ZZZ and so on.
Given a number, convert it to that format and vice versa.
"""
import string

alphabet = string.ascii_uppercase


def _generate_prefix(indices):
    try:
        return ''.join([alphabet[index] for index in indices])
    except:
        a = 1


def reset_previous_index(indices):
    for i in range(len(indices)):
        if indices[-1 - i] == 25:
            indices[-1 - i] = 0
        else:
            indices[-1 - i] += 1
            return False
    return True


def _increment_prefix_indices(indices):
    if len(indices) == 0 or indices[-1] == 25:
        add = reset_previous_index(indices)
        if add:
            indices.append(0)
    else:
        indices[-1] += 1


def convert(number):
    """ does it by iterating through the range
        O(n)
    """

    prefix_indices = []
    result = ''

    for i in range(number):
        if i % 26 == 0 and i != 0:
            _increment_prefix_indices(prefix_indices)
        result = '{}{}'.format(_generate_prefix(prefix_indices), alphabet[i % 26])
    return result


convert(50000)


def find_conversion(number):
    """ could be something with modulo 3 % 26 = C """


