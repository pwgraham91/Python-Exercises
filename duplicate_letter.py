"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase
and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()

        letter_count[lower_letter] = 1 + letter_count.get(lower_letter) if letter_count.get(lower_letter) else 1

    count = 0
    for key, value in letter_count.items():
        if value > 1:
            count += 1

    return count


assert duplicate_count("abcde") == 0
assert duplicate_count("abcdea") == 1
assert duplicate_count("indivisibility") == 1
