__author__ = 'petergraham'


def tictactoe_referee(game_result):
    row = 0
    for x in game_result:
        column = 0
        for y in x:
            current = game_result[row][column]
            if current != ".":
                if row == 0 and game_result[row + 1][column] == current and game_result[row + 2][column] == current:
                    return current
                elif row == 1 and game_result[row - 1][column] == current and game_result[row + 1][column] == current:
                    return current
                elif row == 2 and game_result[row - 2][column] == current and game_result[row - 1][column] == current:
                    return current
                elif column == 0 and game_result[row][column + 1] == current and game_result[row][column + 2] == current:
                    return current
                elif column == 1 and game_result[row][column - 1] == current and game_result[row][column + 1] == current:
                    return current
                elif column == 2 and game_result[row][column - 1] == current and game_result[row][column - 2] == current:
                    return current
                elif row == 0 and column == 0 and game_result[row + 1][column + 1] == current and game_result[row + 2][column + 2] == current:
                    return current
                elif row == 0 and column == 2 and game_result[row + 1][column - 1] == current and game_result[row + 2][column - 2] == current:
                    return current
            column += 1
        row += 1
    return "D"

print tictactoe_referee(
    [
        u"...",
        u"XXX",
        u"XXO"]
)