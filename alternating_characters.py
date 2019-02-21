"""
https://www.hackerrank.com/challenges/alternating-characters/problem
"""


def alter_char(string):
    last_seen = None
    deleted = 0
    for i in range(len(string)):
        if last_seen and last_seen == string[i]:
            deleted += 1
        else:
            last_seen = string[i]
    return deleted


assert alter_char('AABAAB') == 2
assert alter_char('AAAA') == 3
assert alter_char('BBBBB') == 4
assert alter_char('ABABABAB') == 0
assert alter_char('BABABA') == 0
assert alter_char('AAABBB') == 4