"""
A k-palindrome is a string which transforms into a palindrome on removing at most k characters.

Given a string S, and an integer K, print "YES" if S is a k-palindrome; otherwise print "NO".
Constraints:
S has at most 20,000 characters.
0<=k<=30

Sample Test Case#1:
Input - abxa 1
Output - YES
Sample Test Case#2:
Input - abdxa 1
Output - No

"""


def reverse_string(string):
    result = ''
    for i in range(len(string)):
        result = '{}{}'.format(result, string[-1 - i])
    return result


def iterate_and_remove(forwards, removable_characters):
    for i in range(len(forwards)):
        forwards_list = list(forwards)
        forwards_list.pop(i)
        new = ''.join(forwards_list)
        if new == reverse_string(new):
            return True

        if removable_characters > 0:
            iterator = iterate_and_remove(new, removable_characters - 1)
            if iterator:
                return True
    return False


def brute_solve(forwards, removable_characters):
    """
    n^k runtime where k <= n
    """
    if forwards == reverse_string(forwards):
        return True

    if iterate_and_remove(forwards, removable_characters - 1):
        return True
    else:
        return False


assert brute_solve('abxa', 1)
assert not brute_solve('abdxa', 1)
assert brute_solve('abdxa', 2)
assert brute_solve('abbba', 1)
assert brute_solve('abbb33a', 2)
assert brute_solve('nursesrun', 1)
assert not brute_solve('nur3sesr1un', 1)
assert brute_solve('nur3sesr1un', 2)
