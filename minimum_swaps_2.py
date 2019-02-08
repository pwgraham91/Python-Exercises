"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem

You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array
in ascending order.


For example, given the array [7, 1, 3, 2, 4, 5, 6]  we perform the following steps:
i   arr                     swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took 5 swaps to sort the array.

Input:
4
4 3 1 2

Output:
3

Input:
5
2 3 4 1 5

Output:
3
"""


def min_max_swap(array, spaces_from_sorted):
    min_index, max_index = [None, None], [None, None]
    for index, value in enumerate(spaces_from_sorted):
        if min_index[1] is None or value < min_index[1]:
            min_index = [index, value]
        if max_index[1] is None or value > max_index[1]:
            max_index = [index, value]
    if max_index[0] < min_index[0]:
        array[min_index[0]], array[max_index[0]] = array[max_index[0]], array[min_index[0]]
        return
    elif max_index[1] > abs(min_index[1]):
        array[max_index[0]], array[max_index[0] - max_index[1]] = array[max_index[0] - max_index[1]], array[max_index[0]]
    else:
        array[min_index[0]], array[min_index[0] + min_index[1]] = array[min_index[0] + min_index[1]], array[min_index[0]]


def minimum_swaps(arr):
    sorted_array = sorted(arr)
    swaps = 0

    while sorted_array != arr:
        spaces_from_sorted = []

        for index, value in enumerate(arr):
            array_index = arr.index(value)
            sorted_index = sorted_array.index(value)

            spaces_from_sorted.append(sorted_index - array_index)

        # find exact swap
        for index, value in enumerate(spaces_from_sorted):
            if value > 0 and spaces_from_sorted[index + value] == value * -1:
                arr[index], arr[index + value] = arr[index + value], arr[index]
                break
        else:
            min_max_swap(arr, spaces_from_sorted)
        swaps += 1

    return swaps


assert minimum_swaps([7, 1, 3, 2, 4, 5, 6]) == 5
assert minimum_swaps([4, 3, 1, 2]) == 3
assert minimum_swaps([2, 3, 4, 1, 5]) == 3
assert minimum_swaps([3, 7, 6, 9, 1, 8, 10, 4, 2, 5]) == 9
