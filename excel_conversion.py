"""
Microsoft Excel numbers cells as 1...26 and after that AA, AB.... AAA, AAB...ZZZ and so on.
Given a number, convert it to that format and vice versa.
"""
import string

alphabet = string.ascii_uppercase


def _generate_prefix(indices):
    return ''.join([alphabet[index] for index in indices])


def _increment_prefix_indices(indices):
    if len(indices) == 0 or indices[-1] == 26:
        indices.append(0)
    else:
        indices[-1] += 1


def convert(number):

    prefix_indices = []
    result = ''

    for i in range(number):
        if i % 26 == 0 and i != 0:
            _increment_prefix_indices(prefix_indices)
        result = '{}{}'.format(_generate_prefix(prefix_indices), alphabet[i % 26])

        print(result)


# could be something with modulo 3 % 26 = C

convert(500)
