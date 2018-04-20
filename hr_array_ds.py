""" take a list and print the reverse of the list separated by a single space """


def print_reverse(array):
    output = ''
    for index, i in enumerate(array):
        output += '{} '.format(array[len(array) - index - 1])
    output = output[:-1]
    print(output)
    return output


assert print_reverse([1, 2, 3, 4]) == '4 3 2 1'
assert print_reverse([4, 3, 2, 1]) == '1 2 3 4'
assert print_reverse([6676, 3216, 4063, 8373, 423, 586, 8850, 6762]) == '6762 8850 586 423 8373 4063 3216 6676'
assert print_reverse([1]) == '1'
assert print_reverse([]) == ''
