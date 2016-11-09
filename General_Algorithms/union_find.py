
# It's implementation of weighted union_find with quick union implementation.

class UnionFind:
    def __init__(self, components_number):
        self.ids = [x for x in range(components_number)]
        self.size = [1 for _ in range (components_number)]

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

