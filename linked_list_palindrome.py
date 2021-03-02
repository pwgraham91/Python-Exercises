""" determine if the linked list is a palindrome """
from linked_lists import LinkedList


def is_palindrome(linked_list):
    pass


a = LinkedList("c")
b = LinkedList("i")
c = LinkedList("v")
d = LinkedList("i")
b2 = LinkedList("c")
# e = LinkedList("f")
a.insert(b)
b.insert(c)
c.insert(d)
d.insert(b2)
# b2.insert(e)

print(is_palindrome(a) is True)

