from linked_lists import LinkedList

""" determine if any combination of the linked list is a palindrome """

def is_any_combo_ll_palindrome(linked_list):
    num_letters = 0
    unaccounted_letters = set()
    while linked_list is not None:
        num_letters += 1
        current_value = linked_list.val
        if current_value in unaccounted_letters:
            unaccounted_letters.remove(current_value)
        else:
            unaccounted_letters.add(current_value)
        linked_list = linked_list.next
    if num_letters % 2 == 0:
        return len(unaccounted_letters) == 0
    else:
        return len(unaccounted_letters) == 1

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

print(is_any_combo_ll_palindrome(a) is True)
