class LinkedList(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def insert(self, next):
        self.next = next
        next.prev = self
        return self

    def __repr__(self):
        return self.val


def add_links():
    return LinkedList('a').insert(LinkedList('b').insert(LinkedList('c')))


def print_to_end(link):
    print(link.val)
    if link.next:
        print_to_end(link.next)


def find_continue(link, value):
    if link.val == value:
        return link
    else:
        return find_continue(link.next, value)


def search(head, value):
    return find_continue(head, value)
