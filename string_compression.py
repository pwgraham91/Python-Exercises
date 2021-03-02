""" given aabbbcddddeeff return a string that compresses the duplication of characters like this:
a2b3c1d4e2f2
"""

""" O(n) time
    O(n) space for the string list
"""
def compress_string(string):
    if len(string) == 0:
        return ""
    prev_char = string[0]
    char_count = 0
    string_list = []
    for i, char in enumerate(string):
        if prev_char == char:
            char_count += 1
        else:
            string_list.append("{}{}".format(prev_char, char_count))
            char_count = 1
            prev_char = char
    string_list.append("{}{}".format(prev_char, char_count))

    return "".join(string_list)

print(compress_string("aabbbcddddeeff"))
print(compress_string("a"))
