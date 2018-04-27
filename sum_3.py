"""
Given an array of n elements return true if 3 of the sum of 3 elements is equal to a constant c

Example array a[6,2,3,4] constant c = 9

if a[1] + [2] + [3] == c return true

The size of the array is n

If any set of 3 elements is equal to the constant c, then return false

"""


def find_3(array, constant):
    """
     O(n^3)
     longform: O((n-1)^3)
    """

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


def find_3_dict(array, constant):
    """
     average: O(n^2)
     longform: O(n + (n-1)^2)

     worst: O(n^3)
     longform: O(n + (n-1)^3)

     This trades space optimization for time. By adding all of the indices to a dictionary, we only have to do 1
     nested for loop and search the dictionary for the needed number based on the sum of the first 2 numbers.
    """

    mapped_ints = {}
    for i in array:
        if mapped_ints.get(i):
            mapped_ints[i] += 1
        else:
            mapped_ints[i] = 1

    array_len = len(array)
    for count, a in enumerate(array):
        if (array_len < count + 3) or count >= array_len - 2:
            break

        for b in range(array_len - count - 1):
            b_obj = array[count + b + 1]
            needed_number = constant - a - b_obj

            number_frequency = mapped_ints.get(needed_number, 0)
            if number_frequency >= 1 + (1 if needed_number == a else 0) + (1 if needed_number == b_obj else 0):
                return True
    return False



assert find_3([6, 2, 3, 4], 9)
assert find_3([6, 2, 3, 4, 5, 8, 9], 15)
assert not find_3([1, 1, 1, 1, 1], 2)

assert find_3_dict([6, 2, 3, 4], 9)
assert not find_3_dict([1, 1, 1, 1, 1], 2)
assert find_3_dict([6, 2, 3, 4, 5, 8, 9], 15)
assert find_3_dict([-3, -2, -2, -1, 0, 4, -2, 4], 6)
