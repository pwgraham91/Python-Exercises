"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below
matrix contains 5 islands

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5
"""


def hash_coordinates(coordinates):
    return '{},{}'.format(coordinates[0], coordinates[1])


def mark_found(graph, land_coordinates, island_lands, found_lands, original_found_land):
    if land_coordinates not in found_lands:
        if island_lands.get(hash_coordinates(original_found_land)):
            island_lands[hash_coordinates(original_found_land)].append(land_coordinates)
        else:
            island_lands[hash_coordinates(original_found_land)] = [land_coordinates]
        found_lands.append(land_coordinates)
        search_neighbors(graph, land_coordinates, island_lands, found_lands, original_found_land)


def search_neighbors(graph, land_coordinates, island_lands, found_lands, original_found_land):
    search_around_range = [-1, 0, 1]
    for x in search_around_range:
        for y in search_around_range:
            neighbor_x = land_coordinates[0] + x
            neighbor_y = land_coordinates[1] + y

            # must be on the board
            if neighbor_x >= 0 and neighbor_y >= 0:
                neighbor_coordinates = [neighbor_x, neighbor_y]
                try:
                    if graph[neighbor_x][neighbor_y] == 1:
                        mark_found(graph, neighbor_coordinates, island_lands, found_lands, original_found_land)
                except IndexError:
                    pass


def find_islands(graph):
    island_lands = {}
    found_lands = []

    for x, row in enumerate(graph):
        for y, land in enumerate(row):
            if land == 1:
                land_coordinates = [x, y]
                mark_found(graph, land_coordinates, island_lands, found_lands, land_coordinates)
    return len(island_lands.keys())


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

assert find_islands(graph) == 5

graph = [[0, 1, 1, 1, 0],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 1, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1]]

assert find_islands(graph) == 1

graph = [[0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 1, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1]]

assert find_islands(graph) == 2
