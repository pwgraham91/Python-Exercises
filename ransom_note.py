"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""


def ransom(magazine, note):
    words = {}
    for word in magazine.split(' '):
        if words.get(word):
            words[word] += 1
        else:
            words[word] = 1

    for word in note.split(' '):
        if words.get(word):
            words[word] -= 1
            if words[word] == 0:
                del words[word]
        else:
            print('No')
            return False
    print('Yes')
    return True


assert ransom("give me one grand today night", "give one grand today")
assert not ransom("two times three is not four", "two times two is four")
assert not ransom("ive got a lovely bunch of coconuts", "ive got some coconuts")
