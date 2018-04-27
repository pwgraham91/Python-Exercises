"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""


def sum_2_array(nums, target):
    mapped_ints = {}
    for index, i in enumerate(nums):
        if mapped_ints.get(i):
            mapped_ints[i].append(index)
        else:
            mapped_ints[i] = [index]

    for index_a, a in enumerate(nums):
        needed_num = target - a
        mapped_indices = mapped_ints.get(needed_num)
        if mapped_indices:
            if needed_num == a:
                if len(mapped_indices) > 1:
                    mapped_indices.remove(index_a)
                    return [index_a, mapped_indices[0]]
            else:
                return [index_a, mapped_indices[0]]
    return False


assert sum_2_array([6, 2, 5, 4], 9) == [2, 3]
assert sum_2_array([6, 2, 3, 4, 5, 8, 9], 15) == [0, 6]
assert sum_2_array([1, 1, 2], 2) == [0, 1]