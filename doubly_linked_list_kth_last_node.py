import unittest


"""
Write a function kth_to_last_node() that takes an integer kk and the head_node of a linked list, and returns the 
kth to last node in the list.
"""


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def kth_to_last_node(k, base_node):
    current_node = base_node
    while True:
        if current_node.next:
            current_node.next.prev = current_node
            current_node = current_node.next
        else:
            break

    for i in range(k - 1):
        if current_node.prev:
            current_node = current_node.prev
        else:
            return

    return current_node


class Test(unittest.TestCase):
    def setUp(self):
        self.a = LinkedListNode("Angel Food")
        self.b = LinkedListNode("Bundt")
        self.c = LinkedListNode("Cheese")
        self.d = LinkedListNode("Devil's Food")
        self.e = LinkedListNode("Eccles")

        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e

    def test_base_case(self):
        # Returns the node with value "Devil's Food" (the 2nd to last node)
        assert kth_to_last_node(2, self.a).value == "Devil's Food"

    def test_1_case(self):
        assert kth_to_last_node(1, self.a).value == "Eccles"

    def test_5_case(self):
        assert kth_to_last_node(5, self.a).value == "Angel Food"

    def test_n_plus_1_case(self):
        assert kth_to_last_node(10, self.a) is None


unittest.main(verbosity=2)
