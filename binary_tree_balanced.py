""" implement a function to check if a binary tree is balanced (the heights of the two subtrees of any node
 never differ by more than one
"""
from binary_tree_traversal import build_4_layer_even_tree
from binarytree import Node


def is_balanced(node):
    try:
        max_depth(node)
        return True
    except UnbalancedException:
        return False


class UnbalancedException(Exception):
    pass


def build_uneven_tree():
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

    p_node = k_node.insert_left('p')
    q_node = p_node.insert_right('q')

    l_node = f_node.insert_left('l')
    m_node = f_node.insert_right('m')

    n_node = g_node.insert_left('n')
    o_node = g_node.insert_right('o')

    return a_node


def max_depth(node):
    if node is None:
        return -1
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    if abs(left_depth - right_depth) > 1:
        raise UnbalancedException("unbalanced")

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1
print(is_balanced(build_4_layer_even_tree()) is True)
print(is_balanced(build_uneven_tree()) is False)

"""
        __________a______
       /                 \
    __b__               __c__
   /     \             /     \
  d       e____       f       g
 / \     /     \     / \     / \
h   i   j     __k   l   m   n   o
             /
            p
             \
              q
"""
