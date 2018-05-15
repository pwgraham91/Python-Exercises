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
    altered = False
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
            if [r_i, c_i] in unknown_spots:
                unknown_spots.remove([r_i, c_i])
            altered = True
        else:
            # set the None as its list of possible numbers
            hint_matrix[r_i][c_i] = possible_numbers
            # add unknown spots
            if unknown_spots is not None:
                unknown_spots.append([r_i, c_i])
    return altered


def opposing_cell_has_duplicate(opposing_cell, possible_number):
    if type(opposing_cell) == list:
        if possible_number in opposing_cell:
            return True
    return False


def solve(hint_matrix):
    all_possible_numbers = range(1, 10)
    unknown_spots = []

    changed = True
    while changed:
        changed = False
        # keep running through the possibility setter until we've exhausted that method
        for r_i, row in enumerate(hint_matrix):
            for c_i, obj in enumerate(row):
                altered = set_possibilities(r_i, c_i, hint_matrix, all_possible_numbers, unknown_spots)
                if altered:
                    changed = True

    # after exhausting the possibility setter, if there's still unknowns, check the unknown spots
    check_unknown_spots(hint_matrix, unknown_spots, all_possible_numbers)
    return hint_matrix


def check_unknown_spots(hint_matrix, unknown_spots, all_possible_numbers):
    for unknown_spot in unknown_spots:
        possible_numbers = hint_matrix[unknown_spot[0]][unknown_spot[1]]

        if type(possible_numbers) == int:
            continue

        for possible_number in possible_numbers:
            found_duplicate_number = False

            for i in range(9):
                # check row
                opposing_cell_row = unknown_spot[0]
                opposing_cell_column = i
                if not (opposing_cell_row == unknown_spot[0] and opposing_cell_column == unknown_spot[1]):
                    if opposing_cell_has_duplicate(hint_matrix[unknown_spot[0]][i], possible_number):
                        found_duplicate_number = True
                        break

                # check column
                opposing_cell_row = i
                opposing_cell_column = unknown_spot[1]
                if not (opposing_cell_row == unknown_spot[0] and opposing_cell_column == unknown_spot[1]):
                    if opposing_cell_has_duplicate(hint_matrix[unknown_spot[0]][i], possible_number):
                        found_duplicate_number = True
                        break

            if not found_duplicate_number:
                hint_matrix[unknown_spot[0]][unknown_spot[1]] = possible_number
                unknown_spots.remove(unknown_spot)

                for _spot in unknown_spots:
                    set_possibilities(_spot[0], _spot[1], hint_matrix, all_possible_numbers, unknown_spots)

                check_unknown_spots(hint_matrix, unknown_spots, all_possible_numbers)
                return


def validate_group(group):
    for obj in group:
        if type(obj) != int:
            return False
    if len(set(group)) != 9:
        return False
    return True


def validate_sudoku_matrix(matrix):
    for row in matrix:
        if not validate_group(row):
            return False

    for i in range(9):
        # validate columns
        validate_group([row[i] for row in matrix])


validate_sudoku_matrix(solve([
    [None, None, None, 2, 6, None, 7, None, 1],
    [6, 8, None, None, 7, None, None, 9, None],
    [1, 9, None, None, None, 4, 5, None, None],
    [8, 2, None, 1, None, None, None, 4, None],
    [None, None, 4, 6, None, 2, 9, None, None],
    [None, 5, None, None, None, 3, None, 2, 8],
    [None, None, 9, 3, None, None, None, 7, 4],
    [None, 4, None, None, 5, None, None, 3, 6],
    [7, None, 3, None, 1, 8, None, None, None]
]))


validate_sudoku_matrix(solve([
    [4, None, 5, None, 2, None, None, 6, None],
    [6, None, None, 9, None, None, None, 1, 3],
    [None, 9, None, 3, 6, 7, None, None, 5],
    [None, 6, None, 5, None, None, None, None, None],
    [3, None, None, 7, None, 6, None, None, 8],
    [None, None, None, None, None, 8, None, 7, None],
    [8, None, None, 2, 4, 5, None, 9, None],
    [9, 7, None, None, None, 3, None, None, 2],
    [None, 5, None, None, 7, None, 8, None, 6]
]))
