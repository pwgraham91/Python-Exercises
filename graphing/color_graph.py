import json
import sys


class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

    def __repr__(self):
        return '{}:{}'.format(self.label, self.color)


def build_graph_nodes(graph) -> dict:
    nodes_by_label = {}

    for node_set in graph:
        node_a = node_set[0]
        node_b = node_set[1]

        graph_node_a = nodes_by_label.get(node_a)
        if not graph_node_a:
            graph_node_a = GraphNode(label=node_a)
            nodes_by_label[node_a] = graph_node_a

        graph_node_b = nodes_by_label.get(node_b)
        if not graph_node_b:
            graph_node_b = GraphNode(label=node_b)
            nodes_by_label[node_b] = graph_node_b

        graph_node_a.neighbors.add(graph_node_b)
        graph_node_b.neighbors.add(graph_node_a)

    return nodes_by_label


def find_max_colors(nodes_by_label):
    max_neighbors = 0
    for node in nodes_by_label.values():
        node_neighbors = len(node.neighbors)

        max_neighbors = max(max_neighbors, node_neighbors)

    return max_neighbors + 1


def output_colors(nodes_by_label):
    nodes_colors = []
    for node in nodes_by_label.values():
        nodes_colors.append([node.label, node.color])

    return nodes_colors


def color_the_graph(graph):
    nodes_by_label = build_graph_nodes(graph)

    max_colors = find_max_colors(nodes_by_label)
    color_range = range(1, max_colors + 1)

    for node in nodes_by_label.values():

        if not node.color:
            valid_colors = set(color_range)

            for neighbor in node.neighbors:
                if neighbor.color:
                    valid_colors.discard(neighbor.color)

            color = valid_colors.pop()
            node.color = color

    return output_colors(nodes_by_label)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        colors = color_the_graph(json.load(f))
        with open('colors.json', 'w') as output:
            json.dump(colors, output)
