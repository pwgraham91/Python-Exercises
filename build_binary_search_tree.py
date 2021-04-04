class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


def add_value_to_node(node, value):
    if value < node.value:
        if node.left:
            add_value_to_node(node.left, value)
        else:
            node.insert_left(value)
    elif value > node.value:
        if node.right:
            add_value_to_node(node.right, value)
        else:
            node.insert_right(value)


def build_tree_recursively(items):
    head_node = BinaryTreeNode(items[0])
    node = head_node
    for i in items[1:]:
        add_value_to_node(node, i)

    return head_node


def build_tree_iteratively(items):
    head_node = BinaryTreeNode(items.pop(0))

    while len(items):
        value_tuple_or_int = items.pop(0)
        if type(value_tuple_or_int) is tuple:
            node: BinaryTreeNode = value_tuple_or_int[0]
            value: int = value_tuple_or_int[1]
        else:
            node = head_node
            value = value_tuple_or_int

        if value < node.value:
            if node.left:
                items.insert(0, (node.left, value))
            else:
                node.insert_left(value)
        elif value > node.value:
            if node.right:
                items.insert(0, (node.right, value))
            else:
                node.insert_right(value)

    return head_node


if __name__ == "__main__":
    recursive_tree = build_tree_recursively([8, 3, 10, 14, 6, 1, 4, 2, 7, 13])
    iterative_tree = build_tree_iteratively([8, 3, 10, 14, 6, 1, 4, 2, 7, 13])
