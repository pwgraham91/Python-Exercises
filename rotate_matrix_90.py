def rotate_90(matrix):
    new_matrix = [[] for a in range(len(matrix))]
    for a, row in enumerate(matrix):
        for b, char in enumerate(row):
            new_matrix[a].append(matrix[(b*-1) - 1][a])



rotate_90([
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]) == [["g", "d", "a"],
       ["h", "e", "b"],
       ["i", "f", "c"]]
