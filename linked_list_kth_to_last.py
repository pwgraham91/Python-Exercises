""" find the kth to last element in a singly linked list """
import queue

from linked_lists import LinkedList


""" 
time: n
space: k
"""
def find_kth_last(head, k):
    counter = 0
    q = queue.Queue()
    current = head
    while True:
        counter += 1
        if current is None:
            break
        q.put(current)
        if counter > k:
            q.get()
        current = current.next
    return q.get().val


"""
time: n
space: 1 
"""
def find_kth_last_two_pointers(head, k):
    slow_pointer = head
    fast_pointer = head

    for i in range(k):
        fast_pointer = fast_pointer.next

    while True:
        if fast_pointer is None:
            return slow_pointer.val
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next


a = LinkedList("a")
b = LinkedList("b")
c = LinkedList("c")
d = LinkedList("d")
b2 = LinkedList("e")
e = LinkedList("f")
a.insert(b)
b.insert(c)
c.insert(d)
d.insert(b2)
b2.insert(e)

find_kth_last_two_pointers(a, 3)
