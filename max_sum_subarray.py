"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of
integers.

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If
the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""


def max_sum_fun(input_array):
    max_sum = 0
    max_sum_array = []

    for index_a, num in enumerate(input_array):
        max_sum_array_sub = []

        for sub_num_index in range(len(input_array) - index_a):
            sub_num = input_array[sub_num_index + index_a]
            max_sum_array_sub.append(sub_num)

            current_sum = sum(max_sum_array_sub)
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_array = max_sum_array_sub.copy()

    return max_sum, max_sum_array


max_sum, max_sum_array = max_sum_fun([-2, 1, -3, 4, -1, 2, 1, -5, 4])
assert max_sum == 6
assert max_sum_array == [4, -1, 2, 1]

max_sum, max_sum_array = max_sum_fun([])
assert max_sum == 0
assert max_sum_array == []

max_sum, max_sum_array = max_sum_fun([-1, -2, -3, -4])
assert max_sum == 0
assert max_sum_array == []
