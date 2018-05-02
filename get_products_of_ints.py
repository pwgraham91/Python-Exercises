"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!
"""


def get_products_of_all_ints_except_at_index(array):
    product_array = []
    for index_a, a in enumerate(array):
        result = 1
        for index_b, b in enumerate(array):
            if index_a != index_b:
                result *= b
        product_array.append(result)
    return product_array


assert get_products_of_all_ints_except_at_index([1, 7, 3, 4]) == [84, 12, 28, 21]
