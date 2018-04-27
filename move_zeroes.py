"""
Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the
given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order
of all other elements should be same.

Expected time complexity is O(n) and extra space is O(1).
"""


def move_zeroes_to_end(array):
    """
    time: O(n)
    expanded: O(2n)

    space: O(n)
    """
    # create a copy of the array because you can't remove/add items to the array you're iterating over
    copied_array = array.copy()

    removed_items = 0
    for index, i in enumerate(array):
        if i == 0:
            copied_array.pop(index - removed_items)
            removed_items += 1
            copied_array.append(0)

    return copied_array


def optimized_move_zeroes(array):
    """
    iterate over a range and remove and add as you go so you don't need to copy the array

    time: O(n)
    space: O(1)
    """
    removed_items = 0
    for i in range(len(array)):
        if array[i - removed_items] == 0:
            array.pop(i - removed_items)
            removed_items += 1
            array.append(0)

    print(array)
    return array


assert move_zeroes_to_end([1, 2, 0, 4, 3, 0, 5, 0]) == [1, 2, 4, 3, 5, 0, 0, 0]
assert move_zeroes_to_end([1, 2, 0, 0, 0, 3, 6]) == [1, 2, 3, 6, 0, 0, 0]
assert optimized_move_zeroes([1, 2, 0, 4, 3, 0, 5, 0]) == [1, 2, 4, 3, 5, 0, 0, 0]
assert optimized_move_zeroes([1, 2, 0, 0, 0, 3, 6]) == [1, 2, 3, 6, 0, 0, 0]
