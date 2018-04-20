"""
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in
 the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will 
always be at least 2.
The array will always contain letters in only one case.
"""

import string


def find_missing_letter(array):
    alphabet = string.ascii_lowercase
    index_of_alphabet = alphabet.index(array[0].lower())
    for i in array:
        if alphabet[index_of_alphabet] == i.lower():
            index_of_alphabet += 1
        else:
            if i in alphabet:
                return alphabet[index_of_alphabet]
            else:
                return alphabet[index_of_alphabet].upper()


assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'
