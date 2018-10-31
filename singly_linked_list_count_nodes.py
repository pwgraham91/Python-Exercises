"""
Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the
kth to last node in the list.

time complexity: n + n-k (where k < n)
space complexity: 1
"""
import unittest


class SinglyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


def kth_to_last_node(k, base_node):
    current_node = base_node
    num_nodes = 1
    while True:
        if current_node.next:
            current_node = current_node.next
            num_nodes += 1
        else:
            break

    if k > num_nodes:
        return

    current_node = base_node
    for i in range(num_nodes - k):
        current_node = current_node.next

    return current_node


class Test(unittest.TestCase):
    def setUp(self):
        self.a = SinglyLinkedListNode("Angel Food")
        self.b = SinglyLinkedListNode("Bundt")
        self.c = SinglyLinkedListNode("Cheese")
        self.d = SinglyLinkedListNode("Devil's Food")
        self.e = SinglyLinkedListNode("Eccles")

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
