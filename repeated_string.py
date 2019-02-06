"""
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

Sample Input:
aba
10

Sample Output:
7

Sample Input:
a
1000000000000

Sample Output:
1000000000000
"""


def find_repeated_string(string, num_repeat):
    len_string = len(string)
    num_whole_repeat = int(num_repeat / len_string)
    num_remainder = num_repeat % len_string

    num_found_whole = 0
    num_found_remainder = 0

    for i in range(len_string):
        if not (num_whole_repeat or num_remainder > i):
            break

        letter = string[i]
        if letter != 'a':
            continue

        if num_whole_repeat:
            num_found_whole += 1
        if num_remainder > i:
            num_found_remainder += 1

    total = (num_whole_repeat * num_found_whole) + num_found_remainder

    return total


assert find_repeated_string('aba', 10) == 7
assert find_repeated_string('a', 1000000000000) == 1000000000000


def repeatedString(s, n):
    len_string = len(s)
    num_whole_repeat = int(n / len_string)
    num_remainder = n % len_string

    num_found_whole = 0
    num_found_remainder = 0

    for i in range(len_string):
        if not (num_whole_repeat or num_remainder > i):
            break

        letter = string[i]
        if letter != 'a':
            continue

        if num_whole_repeat:
            num_found_whole += 1
        if num_remainder > i:
            num_found_remainder += 1

    total = (num_whole_repeat * num_found_whole) + num_found_remainder

    return total