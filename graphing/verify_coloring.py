# verify that a coloring for an undirected graph does not have any neighbors with the same color.

import json
import sys


def verify_coloring(graph, coloring):
    # make a node -> color map:
    colormap = {}
    for node, color in coloring:
        colormap[node] = color
    # run through the nodes, checking the coloring
    for a, b in graph:
        if colormap[a] == colormap[b]:
            return False
    return True


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        graph = json.load(f)
    with open(sys.argv[2]) as f:
        coloring = json.load(f)
    print(verify_coloring(graph, coloring))
