"""
    Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
    that occur more than once in the input string. Before processing, make sure the input string contains only 
    alphabets (both uppercase and lowercase) and numeric digits.
"""


class InvalidInputException(Exception):
    pass


def count_char_func(string_input):
    # preverification
    if string_input == '':
        return 0

    if not string_input.isalnum():
        raise InvalidInputException

    # Add keys to dict as we go. Upon adding or incrementing, check if the key has already been added one time.
    # If so, we have a duplicate and we should increment the duplicate counter.
    alnums = {}
    duplicate_counter = 0

    for char in string_input:
        current_count = alnums.get(char)
        if current_count:
            alnums[char] += 1
            if current_count == 1:
                duplicate_counter += 1
        else:
            alnums[char] = 1

    return duplicate_counter


""" TESTS """

# normal cases
assert count_char_func('aabbcc') == 3
assert count_char_func('a22cc') == 2
assert count_char_func('') == 0


# exception cases
try:
    # contains spaces and dashes
    count_char_func('these are numeric digits and my phone number is 707-339-0632')
    raise Exception('this function should have raised an InvalidInputException')
except InvalidInputException:
    pass

try:
    # contains spaces
    count_char_func('a b')
    raise Exception('this function should have raised an InvalidInputException')
except InvalidInputException:
    pass

