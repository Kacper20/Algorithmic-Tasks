from __future__ import print_function
from collections import deque


def compute_query():
    values = list(map(int, input().split()))
    nodes_count = values[0]
    adjacency_list = dict([(key, []) for key in range(1, nodes_count + 1)])

    for i in range(values[1]):
        nodes = list(map(int, input().split()))
        if nodes[1] not in adjacency_list[nodes[0]]:
            adjacency_list[nodes[0]].append(nodes[1])
        if nodes[0] not in adjacency_list[nodes[1]]:
            adjacency_list[nodes[1]].append(nodes[0])
    starting_node = int(input())
    visited_array = [-1] * (nodes_count + 1)

    nodes_queue = deque([starting_node])
    last_node_in_level = starting_node
    current_level = 0
    while len(nodes_queue) > 0:
        node = nodes_queue.popleft()
        visited_array[node] = current_level
        not_visited = [x for x in adjacency_list[node] if visited_array[x] == -1 and x not in nodes_queue]
        if node == last_node_in_level:
            current_level += 1
        for subnode in not_visited:
            nodes_queue.append(subnode)
        if len(not_visited) > 0 and last_node_in_level == node:
            last_node_in_level = not_visited[-1]
        elif len(not_visited) == 0 and last_node_in_level == node and len(nodes_queue) > 0:
            last_node_in_level = nodes_queue[-1]

    other_nodes = [x for x in range(1, nodes_count + 1) if x != starting_node]

    for node in other_nodes:
        level = visited_array[node]
        if level >= 0:
            print(level * 6, end=' ')
        else:
            print(-1, end=' ')
    print("")

n = int(input())
for i in range(n):
    compute_query()
