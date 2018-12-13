# generate a fully-connected undirected graph (as JSON)

import sys
import json

node_count = int(sys.argv[1])

graph = set()

for i in range(1, node_count + 1):
    neighbors = set(range(1, node_count + 1))
    neighbors.remove(i)
    for neighbor in neighbors:
        if i < neighbor:
            edge = (i, neighbor)
        else:
            edge = (neighbor, i)
        graph.add(edge)

print(json.dumps(list(graph)))
