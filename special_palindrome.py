"""
https://www.hackerrank.com/challenges/special-palindrome-again/problem
"""


def check_palindrome(string):
    len_string = len(string)
    for i in range(int(len_string / 2)):
        forward = string[i]
        backward = string[-i - 1]
        if forward != backward:
            return False
    return True


def count_palindromes(string):
    palindromes = []
    len_string = len(string)
    for a in range(len_string):
        length = a + 1
        outer = 0
        while outer < len_string:
            builder = []
            using_string = string[outer:]

            if len(using_string) < length:
                break

            for i in range(len(using_string)):
                if len(builder) < length:
                    builder.append(using_string[i])
                else:
                    break
            if check_palindrome(builder):
                palindromes.append(''.join(builder))

            outer += 1

    return len(palindromes)


assert count_palindromes('asasd') == 7
# a s a s d asa sas
assert count_palindromes('abcbaba') == 11
# ['a', 'b', 'c', 'b', 'a', 'b', 'a', 'bcb', 'bab', 'aba', 'abcba']
assert count_palindromes('aaaa') == 10

assert check_palindrome('asa')
assert check_palindrome('assa')
assert check_palindrome('asksa')
assert not check_palindrome('ab')
assert not check_palindrome('abas')
assert not check_palindrome('abc')
