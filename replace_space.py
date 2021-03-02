""" write a function to trim spaces off the end of a string and replace inner spaces with %20
input: "  my name is peter    "
output: "my%20name%20is%20peter"
"""


def find_first_non_space_index(string):
    for i, char in enumerate(string):
        if char != " ":
            return i
    return 100


def trim_string(string):
    core_string = list(string)
    left_space_index = find_first_non_space_index(core_string)
    if left_space_index is not None:
        core_string = core_string[left_space_index:]
    right_space_index = find_first_non_space_index(core_string[::-1])
    if right_space_index is not None:
        core_string = core_string[:(len(core_string) - right_space_index)]
    return core_string


def replace_space(string_list):
    for i, char in enumerate(string_list):
        if char == " ":
            string_list[i] = "%20"
    return string_list


def trim_and_replace(string):
    core_string_list = trim_string(string)
    replaced_string_list = replace_space(core_string_list)

    return "".join(replaced_string_list)

print(trim_and_replace("    ab cd ef    "))
