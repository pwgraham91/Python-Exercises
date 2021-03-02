""" remove duplicates from linked list """
from linked_lists import LinkedList

""" time: n
 space: n
 """
def rm_duplicates(head):
    seen_values = set(head.val)
    current = head
    while True:
        current = current.next
        if current is None:
            break
        if current.val in seen_values:
            current.prev.next = current.next
        else:
            seen_values.add(current.val)

"""
time: n^2
space: 1
"""
def rm_duplicates_space(head):
    current = head
    breaker_one = True
    while breaker_one:
        if current is None:
            break
        breaker_two = True
        tracer_two = current.next
        while breaker_two:
            if tracer_two is None:
                break
            if current.val == tracer_two.val:
                tracer_two.prev.next = tracer_two.next
            tracer_two = tracer_two.next
        current = current.next


a = LinkedList("a")
b = LinkedList("b")
c = LinkedList("c")
d = LinkedList("d")
b2 = LinkedList("b")
e = LinkedList("e")
a.insert(b)
b.insert(c)
c.insert(d)
d.insert(b2)
b2.insert(e)

rm_duplicates_space(a)
a = 1

