__author__ = 'petergraham'


def count_neighbours(grid, row, col):
    spots = []
    if row != 0 and col != 0:
        spot1 = grid[row - 1][col - 1]
        spots.append(spot1)
    if row != 0:
        spot2 = grid[row - 1][col]
        spots.append(spot2)
    if row != 0 and len(grid[0]) > (col + 1):
        spot3 = grid[row - 1][col + 1]
        spots.append(spot3)
    if col != 0:
        spot4 = grid[row][col - 1]
        spots.append(spot4)
    if len(grid[0]) > (col + 1):
        spot6 = grid[row][col + 1]
        spots.append(spot6)
    if len(grid) > (row + 1) and col != 0:
        spot7 = grid[row + 1][col - 1]
        spots.append(spot7)
    if len(grid) > (row + 1):
        spot8 = grid[row + 1][col]
        spots.append(spot8)
    if len(grid) > (row + 1) and len(grid[0]) > (col + 1):
        spot9 = grid[row + 1][col + 1]
        spots.append(spot9)
    counter = 0
    for point in spots:
        if point != 0:
            print(point)
            counter += 1
    return counter

count_neighbours(((1, 2, 3, 4, 5),
                 (6, 7, 8, 9, 10),
                 (11, 12, 13, 14, 15),
                 (16, 17, 18, 19, 20),
                 (21, 22, 23, 24, 25),), 3, 4)
