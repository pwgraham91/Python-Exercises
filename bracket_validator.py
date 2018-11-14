"""
You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces, brackets,
 and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.

Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False

https://www.interviewcake.com/question/python/bracket-validator

runtime:
time: n
space: n

"""
import unittest


def validate_brackets(string):
    opener_counterparts = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    closer_counterparts = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    open_openers = []
    for i in string:
        if opener_counterparts.get(i):
            open_openers.append(i)
        elif closer_counterparts.get(i):
            corresponding_opener = closer_counterparts[i]
            if len(open_openers) == 0:
                return False
            last_opener = open_openers.pop()
            if last_opener != corresponding_opener:
                return False
    return True


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(validate_brackets("{ [ ] ( ) }"))

    def test_islands(self):
        self.assertTrue(validate_brackets("((()))[[[]]]"))

    def test_case_2(self):
        self.assertFalse(validate_brackets("{ [ ( ] ) }"))

    def test_case_3(self):
        self.assertFalse(validate_brackets("{ [ }"))


unittest.main(verbosity=2)
