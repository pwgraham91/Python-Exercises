"""
solve sudoku
"""


def check_cell(row_index, column_index, hint_matrix, possible_numbers):
    if type(hint_matrix[row_index][column_index]) == int:
        try:
            possible_numbers.remove(hint_matrix[row_index][column_index])
        except ValueError:
            pass


def determine_search(index):
    modulo = index % 3
    if modulo == 0:
        search = [index, index + 1, index + 2]
    elif modulo == 1:
        search = [index - 1, index, index + 1]
    else:
        search = [index - 2, index - 1, index]

    return search


def check_square(hint_matrix, r_i, c_i, possible_numbers):
    rows_to_search = determine_search(r_i)
    columns_to_search = determine_search(c_i)

    for row_index in rows_to_search:
        for column_index in columns_to_search:
            check_cell(row_index, column_index, hint_matrix, possible_numbers)


def set_possibilities(r_i, c_i, hint_matrix, all_possible_numbers, unknown_spots=None):
    obj = hint_matrix[r_i][c_i]
    if type(obj) != int:
        possible_numbers = list(all_possible_numbers)
        for i in range(9):
            # check row
            check_cell(r_i, i, hint_matrix, possible_numbers)
            # check column
            check_cell(i, c_i, hint_matrix, possible_numbers)
        check_square(hint_matrix, r_i, c_i, possible_numbers)

        if len(possible_numbers) == 1:
            hint_matrix[r_i][c_i] = possible_numbers[0]
        else:
            # set the None as its list of possible numbers
            hint_matrix[r_i][c_i] = possible_numbers
            # add unknown spots
            if unknown_spots is not None:
                unknown_spots.append([r_i, c_i])


def solve(hint_matrix):
    all_possible_numbers = range(1, 10)
    unknown_spots = []

    for r_i, row in enumerate(hint_matrix):
        for c_i, obj in enumerate(row):
            set_possibilities(r_i, c_i, hint_matrix, all_possible_numbers, unknown_spots)

    for unknown_spot in unknown_spots:
        unknown = hint_matrix[unknown_spot[0]][unknown_spot[1]]
        a = 1


assert solve([
    [4, None, 5, None, 2, None, None, 6, None],
    [6, None, None, 9, None, None, None, 1, 3],
    [None, 9, None, 3, 6, 7, None, None, 5],
    [None, 6, None, 5, None, None, None, None, None],
    [3, None, None, 7, None, 6, None, None, 8],
    [None, None, None, None, None, 8, None, 7, None],
    [8, None, None, 2, 4, 5, None, 9, None],
    [9, 7, None, None, None, 3, None, None, 2],
    [None, 5, None, None, 7, None, 8, None, 6]
]) == []
