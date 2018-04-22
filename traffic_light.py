"""
You're writing code to control your town's traffic lights. You need a function to handle each change from green, to
yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a
string representing the state the light should change to.

For example, update_light('green') should return 'yellow'.
"""
import unittest


def update_light(current):
    reverse_light_order = ['red', 'yellow', 'green']
    return reverse_light_order[reverse_light_order.index(current) - 1]


class TestUpdateLight(unittest.TestCase):
    def test_update_light(self):
        self.assertEqual(update_light('green'), 'yellow')
        self.assertEqual(update_light('yellow'), 'red')
        self.assertEqual(update_light('red'), 'green')
