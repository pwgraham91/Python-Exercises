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


def build_4_layer_even_tree():
    a_node = Node('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left
    d_node = b_node.insert_left('d')
    e_node = b_node.insert_right('e')

    c_node = a_node.right
    f_node = c_node.insert_left('f')
    g_node = c_node.insert_right('g')

    h_node = d_node.insert_left('h')
    i_node = d_node.insert_right('i')

    j_node = e_node.insert_left('j')
    k_node = e_node.insert_right('k')

    l_node = f_node.insert_left('l')
    m_node = f_node.insert_right('m')

    n_node = g_node.insert_left('n')
    o_node = g_node.insert_right('o')

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
    a_node = build_4_layer_even_tree()

    if _bfs_iterative(search_for, a_node, iterator):
        return True
    return False


def _bfs_iterative(search_for, node, queue):
    if node is None:
        return

    # add root
    queue.append(node)

    while queue:
        obj = queue.pop(0)
        if obj.value == search_for:
            return True
        if obj.left is not None:
            queue.append(obj.left)
        if obj.right is not None:
            queue.append(obj.right)


def depth_first_iterative(search_for):
    root = build_4_layer_even_tree()

    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == search_for:
            return True
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return False

"""
        ______a______
       /             \
    __b__           __c__
   /     \         /     \
  d       e       f       g
 / \     / \     / \     / \
h   i   j   k   l   m   n   o
"""

depth_first_iterative('p')
breadth_first_search_iterative('z')
