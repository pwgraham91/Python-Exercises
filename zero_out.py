""" write an algorithm such that if an element in an MxN matrix is 0, its column and row are set to 0 """

"""
time is MxN
space is M + N
"""
def set_to_0(matrix):
    zero_rows = set()
    zero_columns = set()
    for a, row in enumerate(matrix):
        for b, char in enumerate(row):
            if matrix[a][b] == 0:
                zero_rows.add(a)
                zero_columns.add(b)

    # zero out rows
    for row_index in zero_rows:
        for i in range(len(matrix[row_index])):
            matrix[row_index][i] = 0

    # zero out columns
    for column_index in zero_columns:
        for a in range(len(matrix)):
            matrix[a][column_index] = 0

    return matrix

print(set_to_0([
    [1, 2, 0],
    [4, 5, 6],
    [0, 8, 9],
]) == [
    [0, 0, 0],
    [0, 5, 0],
    [0, 0, 0]
])
