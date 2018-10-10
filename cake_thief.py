"""
Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
max_duffel_bag_value(cake_tuples, capacity)
"""
import unittest


def find_best_value_cake(cake_tuples, max_capacity):
    best_value_cake = None
    best_ratio = None

    for cake in cake_tuples:
        if cake[0] > max_capacity:
            continue

        if cake[1] == 0:
            # don't consider cakes without value
            continue
        cake_ratio_value = float(cake[1] / cake[0])

        if best_value_cake is None:
            best_value_cake = cake
            best_ratio = cake_ratio_value
        elif cake_ratio_value > best_ratio:
            best_value_cake = cake
            best_ratio = cake_ratio_value
        elif cake_ratio_value == best_ratio and max_capacity % cake[0] == 0:
            # only replace the cake if it's lighter (so we can fit more cakes!)
            best_value_cake = cake
            best_ratio = cake_ratio_value

    return best_value_cake


def max_duffel_bag_value(cake_tuples, capacity):
    """ time complexity: n + cn where n is the number of cakes and c is capacity
        space complexity: 1
    """
    status = {
        'total_value': 0,
        'capacity': capacity
    }

    if capacity == 0:
        return 0

    while True:
        cake = find_best_value_cake(cake_tuples, status['capacity'])
        if not cake:
            return status['total_value']

        if cake[0] <= status['capacity']:
            status['total_value'] += cake[1]
            status['capacity'] -= cake[0]


class Test(unittest.TestCase):
    def test_base_case(self):
        actual = max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20)
        expected = 555
        self.assertEqual(actual, expected)

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_two_cakes_ten(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
