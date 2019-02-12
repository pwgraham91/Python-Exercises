"""https://www.hackerrank.com/challenges/ctci-bubble-sort/problem"""


def count_bubble_sort_swaps(array):
    swaps = 0
    len_array = len(array)

    while True:
        was_swapped = False
        for index in range(len_array):
            if index == len_array - 1:
                break
            value = array[index]
            if value > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                was_swapped = True
                swaps += 1

        if not was_swapped:
            return swaps


assert count_bubble_sort_swaps([1, 2, 3]) == 0
assert count_bubble_sort_swaps([3, 2, 1]) == 3
