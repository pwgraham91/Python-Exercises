"""
https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/python
"""


def find_path(maze):
    maze = maze.split('\n')

    len_x = len(maze[0])
    len_y = len(maze[1])

    explored_paths = []
    unexplored_paths = [(0, 0)]
    while unexplored_paths:
        path = unexplored_paths.pop()
        x = path[0]
        y = path[1]

        if x == len_x and y == len_y:
            return True

        explored_paths.append(path)

        east = (x - 1, y)
        if x != 0 and east not in explored_paths and east not in unexplored_paths and maze[east[0]][east[1]] != 'W':
            unexplored_paths.append(east)

        west = (x + 1, y)
        if x + 1 != len_x and west not in explored_paths and west not in unexplored_paths and maze[west[0]][west[1]] != 'W':
            unexplored_paths.append(west)

        south = (x, y - 1)
        if y != 0 and south not in explored_paths and south not in unexplored_paths and maze[south[0]][south[1]] != 'W':
            unexplored_paths.append(south)

        north = (x, y + 1)
        if y + 1 != len_y and north not in explored_paths and north not in unexplored_paths and maze[north[0]][north[1]] != 'W':
            unexplored_paths.append(north)

    return False


a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

assert find_path(a)
assert not find_path(b)
assert find_path(c)
assert not find_path(d)
