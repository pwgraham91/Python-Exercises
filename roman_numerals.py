"""
Write a function that accepts an integer value as input and outputs a string representation of that value in roman
numerals
"""


class InvalidNumberError(Exception):
    pass


base_romans = [
    [1, 'I'],
    [5, 'V'],
    [10, 'X'],
    [50, 'L'],
    [100, 'C'],
    [500, 'D'],
    [1000, 'M']
]


def get_limits(number):
    lower_limit = None
    upper_limit = None

    for latin_num, roman_num in base_romans:
        if number >= latin_num:
            lower_limit = [latin_num, roman_num]

        if number < latin_num:
            upper_limit = [latin_num, roman_num]
            break

    return lower_limit, upper_limit


def get_subtractable_number(number, upper_limit):
    for latin_num, roman_num in base_romans:
        if upper_limit[0] - latin_num == number:
            return '{}{}'.format(roman_num, upper_limit[1])


def append_numeral(number, constructed_numeral):
    lower_limit, upper_limit = get_limits(number)

    if lower_limit[0] == number:
        constructed_numeral.append(lower_limit[1])
        number -= lower_limit[0]

    elif get_subtractable_number(number, upper_limit):
        constructed_numeral.append(get_subtractable_number(number, upper_limit))
        number -= number

    else:
        constructed_numeral.append(lower_limit[1])
        number -= lower_limit[0]
    if number == 0:
        return constructed_numeral
    else:
        return append_numeral(number, constructed_numeral)


def to_roman(number):
    if number < 0:
        raise InvalidNumberError('number must be greater than 0')

    constructed_numeral = []

    result = ''.join(append_numeral(number, constructed_numeral))
    return result


to_roman(9)

chart = [
    [1, 'I'],
    [2, 'II'],
    [3, 'III'],
    [4, 'IV'],
    [5, 'V'],
    [6, 'VI'],
    [7, 'VII'],
    [8, 'VIII'],
    [9, 'IX'],
    [10, 'X'],
    [11, 'XI'],
    [12, 'XII'],
    [13, 'XIII'],
    [14, 'XIV'],
    [15, 'XV'],
    [16, 'XVI'],
    [17, 'XVII'],
    [18, 'XVIII'],
    [19, 'XIX'],
    [20, 'XX'],
    [21, 'XXI'],
    [22, 'XXII'],
    [23, 'XXIII'],
    [24, 'XXIV'],
    [25, 'XXV'],
    [26, 'XXVI'],
    [27, 'XXVII'],
    [28, 'XXVIII'],
    [29, 'XXIX'],
    [30, 'XXX'],
    [31, 'XXXI'],
    [32, 'XXXII'],
    [33, 'XXXIII'],
    [34, 'XXXIV'],
    [35, 'XXXV'],
    [36, 'XXXVI'],
    [37, 'XXXVII'],
    [38, 'XXXVIII'],
    [39, 'XXXIX'],
    [40, 'XL'],
    [41, 'XLI'],
    [42, 'XLII'],
    [43, 'XLIII'],
    [44, 'XLIV'],
    [45, 'XLV'],
    [46, 'XLVI'],
    [47, 'XLVII'],
    [48, 'XLVIII'],
    [49, 'XLIX'],
    [50, 'L'],
    [51, 'LI'],
    [52, 'LII'],
    [53, 'LIII'],
    [54, 'LIV'],
    [55, 'LV'],
    [56, 'LVI'],
    [57, 'LVII'],
    [58, 'LVIII'],
    [59, 'LIX'],
    [60, 'LX'],
    [61, 'LXI'],
    [62, 'LXII'],
    [63, 'LXIII'],
    [64, 'LXIV'],
    [65, 'LXV'],
    [66, 'LXVI'],
    [67, 'LXVII'],
    [68, 'LXVIII'],
    [69, 'LXIX'],
    [70, 'LXX'],
    [71, 'LXXI'],
    [72, 'LXXII'],
    [73, 'LXXIII'],
    [74, 'LXXIV'],
    [75, 'LXXV'],
    [76, 'LXXVI'],
    [77, 'LXXVII'],
    [78, 'LXXVIII'],
    [79, 'LXXIX'],
    [80, 'LXXX'],
    [81, 'LXXXI'],
    [82, 'LXXXII'],
    [83, 'LXXXIII'],
    [84, 'LXXXIV'],
    [85, 'LXXXV'],
    [86, 'LXXXVI'],
    [87, 'LXXXVII'],
    [88, 'LXXXVIII'],
    [89, 'LXXXIX'],
    [90, 'XC'],
    [91, 'XCI'],
    [92, 'XCII'],
    [93, 'XCIII'],
    [94, 'XCIV'],
    [95, 'XCV'],
    [96, 'XCVI'],
    [97, 'XCVII'],
    [98, 'XCVIII'],
    [99, 'XCIX'],
    [100, 'C'],
    [101, 'CI']
]


def test_chart():
    for i in chart:

        result = to_roman(i[0])
        if result != i[1]:
            print('{} : {} != {}'.format(i[0], result, i[1]))

test_chart()