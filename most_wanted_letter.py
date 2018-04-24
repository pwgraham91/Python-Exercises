__author__ = 'petergraham'


def get_most_common_letter(text):
    letter_count = {}
    current_high_letter = {
        'letter': None,
        'count': 0
    }
    for letter in text:
        lower_letter = letter.lower()

        letter_count[lower_letter] = 1 + letter_count.get(lower_letter) if letter_count.get(lower_letter) else 1

        if letter_count[lower_letter] > current_high_letter['count']:
            current_high_letter['letter'] = lower_letter
            current_high_letter['count'] = letter_count[lower_letter]

    return current_high_letter['letter']


print(get_most_common_letter("Hello World"))
