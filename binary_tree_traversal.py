import binarytree

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
    a_node = binarytree.Node('a')
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
    print(a_node)

binary_2()
