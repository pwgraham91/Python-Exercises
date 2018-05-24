from binarytree import Node, tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = self.right
            self.right = new_node

    def __repr__(self):
        return '|val: {}, left: {}, right: {}|'.format(self.val, self.left, self.right)


class Solution:
    def __init__(self):
        self.result = []

    def preorder_traversal(self, root):
        if not root:
            return []

        self.result.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

        return self.result

    def inorderTraversal(self, root):
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

    def postorderTraversal(self, root):
        if not root:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]


def binary_1():
    a_node = TreeNode('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left
    b_node.insert_right('d')

    c_node = a_node.right
    c_node.insert_left('e')
    c_node.insert_right('f')

    d_node = b_node.right
    e_node = c_node.left
    f_node = c_node.right


binary_1()


def binary_2():
    a_node = Node('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left
    b_node.insert_right('d')

    c_node = a_node.right
    c_node.insert_left('e')
    c_node.insert_right('f')
    a_node.insert_left('new')

    d_node = b_node.right
    e_node = c_node.left
    f_node = c_node.right
    print(a_node)

# binary_2()


def build_3_layer_even_tree():
    a_node = Node('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left
    b_node.insert_left('d')
    b_node.insert_right('e')

    c_node = a_node.right
    c_node.insert_left('f')
    c_node.insert_right('g')

    return a_node


def _dfs_recursive(search_for, node):
    if node is None:
        return

    if node.value == search_for:
        return True

    search_left = _dfs_recursive(search_for, node.left)
    if search_left:
        return True
    search_right = _dfs_recursive(search_for, node.right)
    if search_right:
        return True


def depth_first_search_recursive(search_for):
    a_node = build_3_layer_even_tree()
    print(a_node)

    if _dfs_recursive(search_for, a_node):
        return True
    return False


def breadth_first_search_iterative(search_for):
    iterator = []
    a_node = build_3_layer_even_tree()
    print(a_node)

    if _bfs_iterative(search_for, a_node, iterator):
        return True
    return False


def add_to_queue(node, iterator):
    if node.left is not None:
        iterator.append(node.left)
    if node.right is not None:
        iterator.append(node.right)


def _bfs_iterative(search_for, node, iterator):
    if node is None:
        return

    # add root
    iterator.append(node)

    add_to_queue(node, iterator)

    while len(search_for) > 0:
        obj = iterator.pop(0)
        print(obj.value)
        if obj.value == search_for:
            return True
        else:
            add_to_queue(obj, iterator)


breadth_first_search_iterative('c')


def breadth_first_search(search_for):
    a_node = build_3_layer_even_tree()
    print(a_node)

    if _bfs_recursive(search_for, a_node):
        return True
    return False

# breadth_first_search('g')
