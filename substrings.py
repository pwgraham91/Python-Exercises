"""
https://www.hackerrank.com/challenges/two-strings/problem
"""


def substring(s1, s2):
    smaller_letters = set()
    larger_letters = set()
    if len(s1) > len(s2):
        smaller_word = s2
        larger_word = s1
    else:
        smaller_word = s1
        larger_word = s2

    for letter in smaller_word:
        smaller_letters.add(letter)

    for letter in larger_word:
        larger_letters.add(letter)

    return bool(smaller_letters.intersection(larger_letters))


assert substring('hello', 'world')
assert not substring('hi', 'world')
