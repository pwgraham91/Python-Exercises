import unittest


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
        current_node = current_node.prev

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


unittest.main(verbosity=2)
