"""
https://www.interviewcake.com/question/python/permutation-palindrome
"""


def palindrome(string):
    counter = {}
    len_string = 0

    for i in string:
        len_string += 1
        if counter.get(i):
            counter[i] += 1
        else:
            counter[i] = 1

    num_odds_allowed = 1 if len_string % 2 != 0 else 0

    for value in counter.values():
        if value % 2 != 0:
            if num_odds_allowed:
                num_odds_allowed -= 1
            else:
                return False

    return True


def palindrome_set(string):
    counter = set()
    len_string = 0

    for i in string:
        if i in counter:
            counter.remove(i)
        else:
            counter.add(i)
        len_string += 1

    num_odds_allowed = 1 if len_string % 2 != 0 else 0

    return len(counter) == num_odds_allowed


assert palindrome_set('civic')
assert palindrome_set('ivicc')
assert not palindrome_set('civil')
assert not palindrome_set('livci')
