"""
Given two strings that represent positive floats or integers, add them together without converting the whole input to a
float

O(n)
"""


def make_zeroes(rng):
    zeroes = ''
    for i in range(rng):
        zeroes = '{}{}'.format(zeroes, 0)

    return zeroes


def make_equal_length(a, b):
    a_int, a_decimal = a.split('.')
    b_int, b_decimal = b.split('.')

    len_a_int = len(a_int)
    len_b_int = len(b_int)
    if len_a_int > len_b_int:
        b_int = '{}{}'.format(make_zeroes(len_a_int - len_b_int), b_int)
    if len_b_int > len_a_int:
        a_int = '{}{}'.format(make_zeroes(len_b_int - len_a_int), a_int)

    len_a_decimal = len(a_decimal)
    len_b_decimal = len(b_decimal)
    if len_a_decimal > len_b_decimal:
        b_decimal = '{}{}'.format(b_decimal, make_zeroes(len_a_decimal - len_b_decimal))
    if len_b_decimal > len_a_decimal:
        a_decimal = '{}{}'.format(a_decimal, make_zeroes(len_b_decimal - len_a_decimal))

    return '{}.{}'.format(a_int, a_decimal), '{}.{}'.format(b_int, b_decimal)


def add_num(a, b):
    a, b = make_equal_length(a, b)

    remainder = 0
    output = ''
    a_len = len(a)
    for a_index in range(a_len):
        reverse_index = a_len - a_index - 1
        a_num = a[reverse_index]
        b_num = b[reverse_index]

        if a_num == '.':
            output = '{}{}'.format('.', output)
            continue

        result = int(remainder) + int(a_num) + int(b_num)
        if result > 9:
            remainder = str(result[0])
            result = str(result[1])
        else:
            remainder = 0
        output = '{}{}'.format(result, output)

    if remainder != 0:
        output = '{}{}'.format(remainder, output)

    return output


assert add_num("3.14", "1.23") == "4.37"
assert add_num("30.14", "1.23") == "31.37"
assert add_num("3.14", "1.234") == "4.374"
