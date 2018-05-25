"""
input [2,3,1,4]
output [12,8,24,6]

Multiply all fields except it's own position.

Restrictions:
1. no use of division
2. complexity in O(n)
"""


def brute_multiply(numbers):
    """ iterate through every position
        n^2
    """
    result = []
    for a in range(len(numbers)):
        product = 1
        for index, b in enumerate(numbers):
            if index != a:
                product *= b
        result.append(product)
    return result


assert brute_multiply([2, 3, 1, 4]) == [12, 8, 24, 6]
