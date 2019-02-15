"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
"""
from statistics import median


def activity_notifications(expenditure, d):
    notices = 0
    median_numbers = []
    current_median = None
    for i in expenditure:
        len_median_numbers = len(median_numbers)

        if len_median_numbers == d:
            median_numbers.pop(0)

        median_numbers.append(i)

        if len_median_numbers >= d - 1:
            if current_median and current_median * 2 <= i:
                notices += 1
            current_median = median(median_numbers)

    return notices


assert activity_notifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2