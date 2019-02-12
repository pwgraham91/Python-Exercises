"""
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""


def max_toys_sorted(prices, money):
    prices.sort()
    i = 0
    for i, value in enumerate(prices):
        if money >= value:
            money -= value
        else:
            return i
    else:
        return i + 1


assert max_toys_sorted([1, 2, 3, 4], 7) == 3
assert max_toys_sorted([1, 12, 5, 111, 200, 1000, 10], 50) == 4
assert max_toys_sorted([100], 10) == 0
assert max_toys_sorted([5], 10) == 1
assert max_toys_sorted([3, 3, 3], 10) == 3

