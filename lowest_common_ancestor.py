"""https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees"""

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

from queue import Queue


def lca(root, v1, v2):
    queue = Queue()
    shortest_path_to_v1 = None
    shortest_path_to_v2 = None
    queue.put([root, []])
    while not queue.empty():
        current_item, path = queue.get()

        if current_item.info == v1:
            path.append(current_item)
            shortest_path_to_v1 = path
        elif current_item.info == v2:
            path.append(current_item)
            shortest_path_to_v2 = path
        if shortest_path_to_v1 and shortest_path_to_v2:
            min_list_size = min(len(shortest_path_to_v1), len(shortest_path_to_v2))

            for i in range(min_list_size):
                if shortest_path_to_v1[min_list_size - i - 1] == shortest_path_to_v2[min_list_size - i - 1]:
                    return shortest_path_to_v2[min_list_size - i - 1]

        if current_item.left:
            new_path = path.copy()
            new_path.append(current_item)
            queue.put([current_item.left, new_path])
        if current_item.right:
            new_path = path.copy()
            new_path.append(current_item)
            queue.put([current_item.right, new_path])

    return root


tree = BinarySearchTree()

arr = [8, 4, 9, 1, 2, 3, 6, 5]

for i in arr:
    tree.create(i)

v = [1, 6]

ans = lca(tree.root, v[0], v[1])
print(ans.info)
