# generate an undirected graph (as JSON) with N nodes and of degree M.
# do this by starting with a fully-connected graph and then removing nodes until you reach degree M.

# A note on notation:
# this is a "digraph": {1:set([2,3]), 2:set(1,3), 3:set(1,2)}
# this is a "flat digraph": [[1,[2,3]],[2,[1,3]],[3,[1,2]]]
# this is a "flat graph": [[1,2],[2,3],[1,3]]

import sys
import json
import random

# generate a fully-connected flat graph with n nodes.
def fully_connected(n):
    graph = set()
    for i in range(1, n+1):
        neighbors = set(range(1, n+1))
        neighbors.remove(i)
        for neighbor in neighbors:
            if i < neighbor:
                edge = (i,neighbor)
            else:
                edge = (neighbor,i)
            graph.add(edge)
    return list(graph)

# flatten a digraph.
# {1:set([2,3]), 2:set(1,3), 3:set(1,2)} -> [[1,[2,3]],[2,[1,3]],[3,[1,2]]]
def flatten_digraph(digraph):
    g = []
    for node, neighbors in digraph.items():
        g.append([node, list(neighbors)])
    return g

# transform a list of edges into a directed graph representation.
# [[1,2],[2,3],[1,3]] -> {1:set([2,3]), 2:set(1,3), 3:set(1,2)}
def flatgraph_to_digraph(edges):
    graph = {}
    for a,b in edges:
        s = graph.get(a, set())
        s.add(b)
        graph[a] = s
        s = graph.get(b, set())
        s.add(a)
        graph[b] = s
    return graph

# calculate the degree of a flat graph.
# [[1,2],[2,3],[1,3]] -> 2
def degree_flatgraph(flatgraph):
    return degree_flatdigraph(flatten_digraph(flatgraph_to_digraph(flatgraph)))

# calculate the degree of a flat digraph.
# [[1,[2,3]],[2,[1,3]],[3,[1,2]]] -> 2
def degree_flatdigraph(flatdigraph):
    d = 0
    for node, neighbors in flatdigraph:
        d = max(d, len(neighbors))
    return d

def degree_of_flatgraph_node(flatgraph, node_id):
    return len(flatgraph_to_digraph(flatgraph)[node_id])

# return a flatgraph with enough nodes removed to meet the desired degree.
def truncate(flatgraph, desired_degree):
    tries = 0
    while degree_flatgraph(flatgraph) > desired_degree and tries < 10000:
        print('try {}'.format(tries))
        tries += 1
        index_to_remove = random.choice(range(len(flatgraph)))
        edge = flatgraph[index_to_remove]
        if degree_of_flatgraph_node(flatgraph, edge[0]) > desired_degree and degree_of_flatgraph_node(flatgraph, edge[1]) > desired_degree:
            del flatgraph[index_to_remove]
    if tries >= 10000:
        raise Exception("Infinite loop")
    return flatgraph


if __name__ == "__main__":
    nodecount = int(sys.argv[1])
    degree = int(sys.argv[2])
    graph = truncate(fully_connected(nodecount), degree)
    with open('graph-{}-{}.json'.format(nodecount, degree), 'w') as output:
        json.dump(graph, output)
