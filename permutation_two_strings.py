""" given two strings, determine if one is a permutation of the other """


"""
sort the strings in place. If they are permutations of each other, they should be equal.
n log n time
n space for converting the strings into lists 
 """
def is_string_permutation_of_string_space(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    list_a = list(string_a)
    list_b = list(string_b)
    list_a.sort()
    list_b.sort()
    return list_a == list_b


print(is_string_permutation_of_string_space("abcd", "dcab"))
print(is_string_permutation_of_string_space("abcd", "dcae"))
print(is_string_permutation_of_string_space("abcd", "dcabb"))

""" count the occurrences of each character and compare """
def is_string_permutation_of_string_time(string_a, string_b):
    pass
