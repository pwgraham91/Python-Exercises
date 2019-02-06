"""
https://www.hackerrank.com/challenges/2d-array/problem
"""


def find_sum_hourglasses(arr):
    len_array_of_arrays = len(arr)
    len_row = len(arr[0])

    max_hourglass = None

    for row_i, row in enumerate(arr):
        if row_i == 0 or row_i + 1 == len_array_of_arrays:
            continue
        for column_i, value in enumerate(row):
            if column_i == 0 or column_i + 1 == len_row:
                continue
            hourglass_value = 0
            for i in range(column_i - 1, column_i + 2):
                hourglass_value += arr[row_i - 1][i]
                hourglass_value += arr[row_i + 1][i]
            hourglass_value += value

            max_hourglass = hourglass_value if max_hourglass is None else max(max_hourglass, hourglass_value)

    return max_hourglass


assert find_sum_hourglasses(
    [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]
) == -6

assert find_sum_hourglasses(
    [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
) == 19

