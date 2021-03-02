""" the 2 linked lists given each represent a number where each digit is a node in the linked list in reverse order.
 Add the two numbers.
 ex: 4->2->8 = 824
 +
     2->3->1 = 132
 =             956
 """
from linked_lists import LinkedList


def add_digits(n1, n2):
    n1_current_node = n1
    n2_current_node = n2
    sum_linked_list = None
    carryover = 0
    while n1_current_node is not None or n2_current_node is not None:
        digit_sum = carryover
        carryover = 0
        if n1_current_node is not None:
            digit_sum += n1_current_node.val
            n1_current_node = n1_current_node.next
        if n2_current_node is not None:
            digit_sum += n2_current_node.val
            n2_current_node = n2_current_node.next
        if digit_sum >= 10:
            carryover = 1
            digit_sum -= 10

        next_link = LinkedList(digit_sum)
        next_link.next = sum_linked_list
        sum_linked_list = next_link

    concat_num = []
    if carryover == 1:
        concat_num.append(1)

    while sum_linked_list is not None:
        concat_num.append(sum_linked_list.val)
        sum_linked_list = sum_linked_list.next
    return int("".join([str(i) for i in concat_num]))

a = LinkedList(4)
b = LinkedList(2)
c = LinkedList(8)
a.insert(b)
b.insert(c)


a2 = LinkedList(2)
b2 = LinkedList(3)
c2 = LinkedList(3)
a2.insert(b2)
b2.insert(c2)

print(add_digits(a, a2) == 1156)
