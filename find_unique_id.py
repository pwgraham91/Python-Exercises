"""
Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
https://www.interviewcake.com/question/python/find-unique-int-among-duplicates
"""

import random


def generate_log():
    original_list = list(range(1, 11))
    return_list = original_list.copy()
    return_list.pop(3)
    log = original_list + return_list
    random.shuffle(log)
    return log


def find_unique_id_cycling(log):
    """
    Iterates through the whole list once for each of the items in the list. Adds 1 to a counter per iteration through
    the list and if the counter = 1, that is the unique instance.
    time complexity: n^2
    space complexity: 1
    """
    comparison_count = 0
    for checking in log:
        found_instances = 0

        for comparison in log:
            comparison_count += 1
            if checking == comparison:
                found_instances += 1

        if found_instances == 1:
            print(comparison_count)
            return checking


def find_unique_cycling_reduction(log):
    """
    time complexity: (((n-1) / 2) ^ 2) + (n-1) / 2
    why? n - 1 / 2 is the number of ids, ^2 because you need to trace through the list recursively but /2 because
    you're reducing the list as you go
    space complexity: 1
    """
    copied_log = log.copy()
    comparison_count = 0

    while len(copied_log) > 0:
        checking = copied_log[0]
        for i in range(1, len(copied_log)):
            comparison = copied_log[i]
            comparison_count += 1
            if checking == comparison:
                # remove the found ids from the copied list
                copied_log.pop(i)
                copied_log.pop(0)
                break
        else:
            print(comparison_count)
            return checking


def find_unique_dict(log):
    """
    time complexity: n
    space complexity: n
    """
    duplicate_dict = {}
    for i in log:
        if duplicate_dict.get(i):
            duplicate_dict.pop(i)
        else:
            duplicate_dict[i] = 1
    return list(duplicate_dict)[0]


def find_unique_sort(log):
    """
    time complexity: nlogn + (n-1)
    space complexity: 1
    """
    log.sort()
    for a in range(len(log)):
        try:
            if log[0] == log[1]:
                log.pop(1)
                log.pop(0)
            else:
                return log[a]
        except IndexError:
            return log[0]


def find_unique_crazy_xor(delivery_ids):
    """
    time complexity: n
    space complexity: 1
    """

    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id


test_list = [4, 3, 7, 2, 6, 5, 9, 9, 2, 7, 8, 5, 1, 8, 1, 3, 10, 6, 10]
print('cycling beginning of the list: n where n={}'.format(len(test_list)))
print('result: ', find_unique_id_cycling(test_list))

test_list = [3, 7, 2, 6, 5, 9, 9, 2, 7, 8, 5, 1, 8, 1, 3, 10, 6, 10, 4]
print('cycling end of the list: n^2 . where n={}'.format(len(test_list)))
print('result: ', find_unique_id_cycling(test_list))

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
print('cycling end of the palindromic list, n^2 . where n={}'.format(len(test_list)))
print('result: ', find_unique_id_cycling(test_list))

test_list = [4, 3, 7, 2, 6, 5, 9, 9, 2, 7, 8, 5, 1, 8, 1, 3, 10, 6, 10]
print('reduction beginning of the list, n . where n={}'.format(len(test_list)))
print('result: ', find_unique_cycling_reduction(test_list))

test_list = [3, 7, 2, 6, 5, 9, 9, 2, 7, 8, 5, 1, 8, 1, 3, 10, 6, 10, 4]
print('reduction end of the list, random . where n={}'.format(len(test_list)))
print('result: ', find_unique_cycling_reduction(test_list))

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('reduction worst case, (((n-1) / 2) ^ 2) + (n-1) / 2 . where n={}'.format(len(test_list)))
print('result: ', find_unique_cycling_reduction(test_list))

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
print('reduction worst case, (((n-1) / 2) ^ 2) + (n-1) / 2 . where n={}'.format(len(test_list)))
print('result: ', find_unique_cycling_reduction(test_list))

print('dict worst case, n where n={}'.format(len(test_list)))
print('result: ', find_unique_dict(test_list))

print('sort worst case, nlog(n) + (n-1) where n={}'.format(len(test_list)))
print('result: ', find_unique_sort(test_list))

print('xor worst case, n where n={}'.format(len(test_list)))
print('result: ', find_unique_crazy_xor(test_list))
