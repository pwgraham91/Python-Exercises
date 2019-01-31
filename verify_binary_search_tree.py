#!/usr/bin/env python

# some unit tests for https://www.interviewcake.com/question/python/bst-checker
from build_binary_search_tree import build_tree_iteratively, BinaryTreeNode


def verify(root):
    if not root:
        return False

    nodes = [(root, None, None)]

    while nodes:
        node_min_max = nodes.pop(0)

        node: BinaryTreeNode = node_min_max[0]
        node_min: int = node_min_max[1]
        node_max: int = node_min_max[2]

        if node.right:
            if node.right.value <= node.value or (node_max and node_max <= node.right.value):
                return False

            tuple_right = node.right
            tuple_right_min = min(node_min, node.value) if node_min else node.value
            tuple_right_max = node_max
            node_tuple = (tuple_right, tuple_right_min, tuple_right_max)

            nodes.insert(0, node_tuple)

        if node.left:
            if node.left.value >= node.value or (node_min and node_min >= node.left.value):
                return False

            tuple_left = node.left
            tuple_left_min = node_min
            tuple_left_max = max(node_max or 0, node.value)
            node_tuple = (tuple_left, tuple_left_min, tuple_left_max)

            nodes.insert(0, node_tuple)

    return True


def test1():
    # tree:
    #  <nil>
    assert verify(None) is False


def test2():
    # tree:
    #   5
    root = BinaryTreeNode(5)
    assert verify(root) is True


def test3():
    # tree:
    #   5
    #  /
    # 3
    root = BinaryTreeNode(5)
    root.insert_left(3)
    assert verify(root) is True


def test4():
    # tree:
    #   5
    #  /
    # 6
    root = BinaryTreeNode(5)
    root.insert_left(6)
    assert verify(root) is False


def test5():
    # tree:
    #     5
    #    /
    #   3
    #  /
    # 2
    root = BinaryTreeNode(5)
    node = root.insert_left(3)
    node.insert_left(2)
    assert verify(root) is True


def test6():
    # tree:
    #     5
    #    /
    #   3
    #  / \
    # 2   1
    root = BinaryTreeNode(5)
    node = root.insert_left(3)
    node.insert_left(2)
    node.insert_right(1)
    assert verify(root) is False


def test7():
    # tree:
    #     5
    #    /
    #   3
    #  / \
    # 2   4
    root = BinaryTreeNode(5)
    node = root.insert_left(3)
    node.insert_left(2)
    node.insert_right(4)
    assert verify(root) is True


def test8():
    # tree:
    #     5
    #    /
    #   3
    #  / \
    # 2   6
    root = BinaryTreeNode(5)
    node = root.insert_left(3)
    node.insert_left(2)
    node.insert_right(6)
    assert verify(root) is False


def test9():
    #        8
    #      /   \
    #     3     10
    #    /  \     \
    #   1    6     14
    #    \   / \    /
    #     2  4  7 13

    root = build_tree_iteratively([8, 3, 10, 14, 6, 1, 4, 2, 7, 13])
    assert verify(root)


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
