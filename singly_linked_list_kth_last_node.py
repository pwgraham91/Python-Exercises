"""
Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the
kth to last node in the list.

time complexity: n
space complexity: k where k < n
"""
import unittest


class SinglyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


def kth_to_last_node(k, base_node):
    nodes = [base_node]

    current_node = base_node
    nodes_size_has_reached_k = False
    while True:
        if current_node.next:
            current_node = current_node.next

            nodes.append(current_node)

            if nodes_size_has_reached_k or len(nodes) > k:
                nodes_size_has_reached_k = True
                # reduce size of nodes because we only need to look back k times
                nodes.pop(0)
        else:
            break

    if k > len(nodes):
        return

    return nodes[0]


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
