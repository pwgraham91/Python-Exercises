"""
Given an array of n elements return true if 3 of the sum of 3 elements is equal to a constant c

Example array a[6,2,3,4] constant c = 9

if a[1] + [2] + [3] == c return true

The size of the array is n

If any set of 3 elements is equal to the constant c, then return false

"""

def find_3(array):

    for count, i in enumerate(array):
        pass



assert find_3([6, 2, 3, 4])
assert find_3([6, 2, 3, 4, 5, 5, 5])
assert not find_3([1, 1, 1, 1, 1])
