"""
https://www.hackerrank.com/challenges/count-triplets-1/problem
"""


def find_triplet(arr, current_index, ratio, triplet, full_triplets):
    current_number = int(arr[current_index])
    target = current_number * ratio
    for index, value in enumerate(arr[current_index:]):
        value = int(value)
        if index == 0:
            continue
        if value == target:
            original_triplet = triplet.copy()
            triplet.append(current_index + index)
            if len(triplet) == 3:
                full_triplets.append(triplet)
                if len(arr) > (current_index + index + 1) and arr[current_index + index + 1] == target:
                    original_triplet.append(current_index + index + 1)
                    full_triplets.append(original_triplet)
                return
            elif len(arr) > (current_index + index + 1) and arr[current_index + index + 1] == target:
                original_triplet.append(current_index + index + 1)
                find_triplet(arr, current_index + index + 1, ratio, original_triplet, full_triplets)
            target = value * ratio


def count_triplets(arr, r):
    full_triplets = []
    for i in range(len(arr)):
        find_triplet(arr, i, r, [i], full_triplets)
    return len(full_triplets)


assert count_triplets([1, 2, 2, 4], 2) == 2
assert count_triplets([1, 3, 9, 9, 27, 81], 3) == 6
assert count_triplets([1, 5, 5, 25, 125], 5) == 4