"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
"""


def make_anagrams(a, b):
    letters = {}
    for letter in a:
        if letters.get(letter):
            letters[letter]['a'] += 1
        else:
            letters[letter] = {
                'a': 1,
                'b': 0
            }

    for letter in b:
        if letters.get(letter):
            letters[letter]['b'] += 1
        else:
            letters[letter] = {
                'a': 0,
                'b': 1
            }

    deletions = 0
    for key, value in letters.items():
        deletions += abs(value['a'] - value['b'])

    return deletions


assert make_anagrams('cde', 'abc') == 4
