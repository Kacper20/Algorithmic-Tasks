import sys

class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

class Graph:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.edges = [[] for _ in range(vertices_count + 1) ]

    def add_edge(self, i, j, weight):
        self.edges[i].append(Edge(j, weight))
        self.edges[j].append(Edge(i, weight))

    def minimum_spanning_tree(self, starting_node):
        is_in_tree = [False] * (self.vertices_count + 1)
        distance = [sys.maxsize] * (self.vertices_count + 1) # its cost of adding vertex i to the tree

        # initial setup
        current_vertex = starting_node
        distance[starting_node] = 0
        sum_weight = 0

        while is_in_tree[current_vertex] is False:
            is_in_tree[current_vertex] = True
            v_edges = self.edges[current_vertex]
            # Fix all of the distances, if adding current vertex changes values
            for edge in v_edges:
                if distance[edge.to] > edge.weight and is_in_tree[edge.to] is False:
                    distance[edge.to] = edge.weight

            next_vertex = -1
            temp_distance = sys.maxsize
            # Find the least costing edge and go with it.
            for i in range(1, self.vertices_count + 1):
                if is_in_tree[i] is False and temp_distance > distance[i]:
                    temp_distance = distance[i]
                    next_vertex = i
            current_vertex = next_vertex
            if next_vertex != -1:
                sum_weight += temp_distance
            else:
                break
        return sum_weight

nodes, edges = map(int, input().strip().split(' '))
graph = Graph(nodes)

for i in range(edges):
    i, j, weight = map(int, input().strip().split(' '))
    graph.add_edge(i, j, weight)

starting_node = int(input())

print(graph.minimum_spanning_tree(starting_node))