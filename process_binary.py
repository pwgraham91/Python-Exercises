"""
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1
"""


def binary_array_to_number(array):
    output = ''
    for i in array:
        output += str(i)
    return int(output, 2)


assert binary_array_to_number([0, 0, 0, 1]) == 1
assert binary_array_to_number([0, 0, 1, 0]) == 2
assert binary_array_to_number([1, 1, 1, 1]) == 15
assert binary_array_to_number([0, 1, 1, 0]) == 6
