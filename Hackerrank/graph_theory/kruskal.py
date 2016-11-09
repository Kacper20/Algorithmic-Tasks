
# It's implementation of weighted union_find with quick union implementation.

class UnionFind:
    def __init__(self, components_number):
        self.ids = [x for x in range(components_number)]
        self.size = [1 for _ in range(components_number)]

    #Returns root of the component
    def find(self, component):
        temp_component = component
        while self.ids[temp_component] is not temp_component:
            temp_component = self.ids[temp_component]
        return temp_component

    def are_connected(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i is parent_j:
            return
        if self.size[parent_i] < self.size[parent_j]:
            self.ids[parent_i] = parent_j
            self.size[parent_j] += self.size[parent_i]
        else:
            self.ids[parent_j] = parent_i
            self.size[parent_i] += self.size[parent_j]


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.edges = []

    def add_edge(self, i, j, weight):
        self.edges.append(Edge(i, j, weight))

    def minimum_spanning_tree(self):
        union_find = UnionFind(self.vertices_count + 1)
        edges_copy = sorted(self.edges, key=lambda edge: edge.weight)
        weight_sum = 0
        for edge in edges_copy:
            if not union_find.are_connected(edge.source, edge.destination):
                union_find.union(edge.source, edge.destination)
                weight_sum += edge.weight
        return weight_sum


nodes, edges = map(int, input().strip().split(' '))
graph = Graph(nodes)

for i in range(edges):
    i, j, weight = map(int, input().strip().split(' '))
    graph.add_edge(i, j, weight)

print(graph.minimum_spanning_tree())