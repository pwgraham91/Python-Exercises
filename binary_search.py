def run(list, target):
    minimum_index = 0
    max_index = len(list) - 1

    if list[max_index] == target:
        return max_index

    while minimum_index <= max_index:
        middle_index = (minimum_index + max_index) // 2
        middle_value = list[middle_index]
        if target > middle_value:
            if minimum_index == middle_index:
                return None
            minimum_index = middle_index
        elif target < middle_value:
            if max_index == middle_index:
                return None
            max_index = middle_index
        else:
            return middle_index


print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 13) == None)
print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 0) == None)
print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 2) == None)
print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 32.5) == None)
print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 4) == 1)
print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 12) == 4)
print(run([1, 4, 8, 10, 12, 15, 30, 32, 33], 33) == 8)
