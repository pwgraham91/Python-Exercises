"""
Given a binary tree, return the preorder traversal of its nodes' values.

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
