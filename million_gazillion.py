"""
I'm making a search engine called MillionGazillion™.

I wrote a crawler that visits web pages, stores a few keywords in a database, and follows links to other web pages. I noticed that my crawler was wasting a lot of time visiting the same pages over and over, so I made a set, visited, where I'm storing URLs I've already visited. Now the crawler only visits a URL if it hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents' basement (where I totally don't live anymore), and it keeps running out of memory because visited is getting so huge.

How can I trim down the amount of space taken up by visited?
"""

sites = ['donut.com', 'donut.com', 'dogood.com', 'dog.com', 'doowop.ninja']


class Trie:
    def __init__(self, value):
        self.val = value
        self.children = []

    def add_child(self, trie):
        self.children.append(trie)

    def __repr__(self):
        if len(self.children):
            return '{} {}'.format(self.val, self.children)
        return self.val


def build_sample_trie():
    initial = Trie('d')

    second = Trie('o')
    initial.add_child(second)

    third = Trie('n')
    second.add_child(third)

    three_a = Trie('g')
    second.add_child(three_a)


def find_or_add_child(trie, string):
    found = False
    for value in trie.children:
        if value.val == string[0]:
            found = True
            if len(string) == 1:
                end = Trie('*')
                value.add_child(end)
            else:
                find_or_add_child(value, string[1:])
    if not found:
        # build rest of trie
        child = Trie(string[0])
        trie.add_child(child)
        if len(string) > 1:
            find_or_add_child(child, string[1:])
        else:
            end = Trie('*')
            child.add_child(end)


def build_trie(sites):
    initial = Trie('$')

    for site in sites:
        find_or_add_child(initial, site)

    return initial


# todo make it so it checks if the sequence already exists
final = build_trie(sites)