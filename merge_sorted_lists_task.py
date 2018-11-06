"""
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Returns [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
merge_lists(my_list, alices_list)
"""


def merge_sorted_lists_pop_method(list_1, list_2):
    """
    pops off the lowest number between the two lists until both original lists are empty
    time complexity: n^2/2 where n is the biggest list
    space: complexity: n where n is the length of the biggest list
    """
    new_list = []

    cp_list_1 = list_1.copy()
    cp_list_2 = list_2.copy()

    while len(cp_list_1) > 0 or len(cp_list_2) > 0:
        if len(cp_list_1) > 0 and len(cp_list_2) > 0:
            # find lowest between 2
            if cp_list_1[0] < cp_list_2[0]:
                new_list.append(cp_list_1.pop(0))
            else:
                new_list.append(cp_list_2.pop(0))
        # if there is only one list with values left...
        elif len(cp_list_1) > 0:
            new_list.append(cp_list_1.pop(0))
        else:
            new_list.append(cp_list_2.pop(0))

    return new_list


assert merge_sorted_lists_pop_method([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# different length of lists
assert merge_sorted_lists_pop_method([3, 4, 6, 7, 10, 11, 15], [1, 5, 8, 12, 14, 19]) == [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 19]
# empty list
assert merge_sorted_lists_pop_method([], [1, 5, 8, 12, 14, 19]) == [1, 5, 8, 12, 14, 19]
# 2 empty lists
assert merge_sorted_lists_pop_method([], []) == []


def merge_sorted_lists_pop_place_method(list_1, list_2):
    """
    instead of popping which incurs n runtime every time, keep track of the place where we should pop and add that
    value to the new sorted list
    time complexity: n where n is the biggest list
    space: complexity: n where n is the length of the biggest list
    """
    new_list = []

    list_1_pop_place = 0
    list_2_pop_place = 0

    while len(list_1) > list_1_pop_place or len(list_2) > list_2_pop_place:
        if len(list_1) > list_1_pop_place and len(list_2) > list_2_pop_place:
            # find lowest between 2
            if list_1[list_1_pop_place] < list_2[list_2_pop_place]:
                new_list.append(list_1[list_1_pop_place])
                list_1_pop_place += 1
            else:
                new_list.append(list_2[list_2_pop_place])
                list_2_pop_place += 1
        # if there is only one list with values left...
        elif len(list_1) > list_1_pop_place:
            new_list.append(list_1[list_1_pop_place])
            list_1_pop_place += 1
        else:
            new_list.append(list_2[list_2_pop_place])
            list_2_pop_place += 1

    return new_list


assert merge_sorted_lists_pop_place_method([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# different length of lists
assert merge_sorted_lists_pop_place_method([3, 4, 6, 7, 10, 11, 15], [1, 5, 8, 12, 14, 19]) == [1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 19]
# empty list
assert merge_sorted_lists_pop_place_method([], [1, 5, 8, 12, 14, 19]) == [1, 5, 8, 12, 14, 19]
# 2 empty lists
assert merge_sorted_lists_pop_place_method([], []) == []
