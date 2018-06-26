"""
I like parentheticals (a lot).

"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).
"""


def find_closing_parens(string, opening_position):
    open_parens = 1

    for count, i in enumerate(string[opening_position + 1:]):
        if i == '(':
            open_parens += 1
        elif i == ')':
            open_parens -= 1
            if open_parens == 0:
                print(count + opening_position)
                return count + opening_position + 1

    print('does not return')
    return False


assert find_closing_parens(
    "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.",
    10) == 79
