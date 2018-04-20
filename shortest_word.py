"""
Given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(string):
    shortest_word_length = None
    for word in string.split(' '):
        len_word = len(word)
        if shortest_word_length is None or len_word < shortest_word_length:
            shortest_word_length = len_word
    return shortest_word_length


assert find_short("bitcoin take over the world maybe who knows perhaps") == 3
assert find_short("turns out random test cases are easier than writing out basic ones") == 3
assert find_short("lets talk about javascript the best language") == 3
assert find_short("i want to travel the world writing code one day") == 1
assert find_short("Lets all go on holiday somewhere very cold") == 2
