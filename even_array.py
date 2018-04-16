"""
Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index
that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
An empty array should be treated like a 0 in this problem.
"""


def find_even_index_simple(input_array):
    for counter, i in enumerate(input_array):
        if sum(input_array[:counter]) == sum(input_array[counter + 1:]):
            return counter


assert find_even_index_simple([1, 2, 3, 4, 3, 2, 1]) == 3
assert find_even_index_simple([1, 100, 50, -51, 1, 1]) == 1
assert find_even_index_simple([20, 10, -80, 10, 10, 15, 35]) == 0


def find_even_index_performant(input_array):
    left_side_sum = 0
    right_side_sum = sum(input_array)

    for counter, i in enumerate(input_array):
        right_side_sum -= i
        if left_side_sum == right_side_sum:
            return counter
        left_side_sum += i


assert find_even_index_performant([1, 2, 3, 4, 3, 2, 1]) == 3
assert find_even_index_performant([1, 100, 50, -51, 1, 1]) == 1
assert find_even_index_performant([20, 10, -80, 10, 10, 15, 35]) == 0
