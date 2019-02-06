"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

A left rotation operation on an array shifts each of the array's elements n unit to the left. For example, if 2 left
rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

"""


def rotate_left(array, rotations):
    return array[rotations:] + array[:rotations]


assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
