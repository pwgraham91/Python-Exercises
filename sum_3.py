"""
Given an array of n elements return true if 3 of the sum of 3 elements is equal to a constant c

Example array a[6,2,3,4] constant c = 9

if a[1] + [2] + [3] == c return true

The size of the array is n

If any set of 3 elements is equal to the constant c, then return false

"""


def find_3(array, constant):

    array_len = len(array)
    for count, a in enumerate(array):
        if (array_len < count + 3) or count >= array_len - 2:
            break

        for b in range(array_len - count - 1):
            for c in range(array_len - count - b - 2):
                b_obj = array[count + b + 1]
                c_obj = array[count + b + c + 2]
                current_sum = a + b_obj + c_obj
                if current_sum == constant:
                    return True
    return False


assert find_3([6, 2, 3, 4], 9)
assert find_3([6, 2, 3, 4, 5, 8, 9], 15)
assert not find_3([1, 1, 1, 1, 1], 2)
