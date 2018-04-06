"""
a: 6 3
b: 1 3 2 6 1 2

Find the number of pairs in list b that are divisible by a number in list a
"""

divis = 2
arr = [5, 9, 10, 7, 4]
divisible_pairs = []

for outer_index, outer_value in enumerate(arr):
    for inner_index, inner_value in enumerate(arr):
        if outer_index == inner_index:
            continue
        elif sorted([outer_index, inner_index]) in divisible_pairs:
            continue
        if (outer_value + inner_value) % divis == 0:
            divisible_pairs.append(sorted([outer_index, inner_index]))
            break
print len(divisible_pairs)
