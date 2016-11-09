from collections import deque


class LocationWithWandMoves:
    def __init__(self, i, j, passes):
        self.i = i
        self.j = j
        self.passes = passes


def locations_to_explore(row, column, grid, visited):
    visited[row][column] = 1
    array = []
    # Could check visited inside recursive call but wanted to optimise it a bit
    if column - 1 >= 0 and not visited[row][column - 1]:
        array.append((row, column - 1))
    if column + 1 < columns and not visited[row][column + 1]:
        array.append((row, column + 1))
    if row - 1 >= 0 and not visited[row - 1][column]:
        array.append((row - 1, column))
    if row + 1 < rows and not visited[row + 1][column]:
        array.append((row + 1, column))
    return list(filter(lambda tup: grid[tup[0]][tup[1]] != "X", array))

def determine_if_impresses(grid, times):
    columns = len(grid)
    rows = len(grid[0])
    visited = [[0 for _ in range(rows)] for _ in range(columns)]
    starting_i = 0
    starting_j = 0
    for i in range(columns):
        for j in range(rows):
            if grid[i][j] == "M":
                starting_i = i
                starting_j = j
                break
    queue = deque()
    queue.append(LocationWithWandMoves(starting_i, starting_j, 0))
    visited[starting_i][starting_j] = 1
    while len(queue) > 0:
        top_location = queue.popleft()
        if grid[top_location.i][top_location.j] == "*":
            return times == top_location.passes
        to_explore = locations_to_explore(top_location.i, top_location.j, grid, visited)
        value_to_add = 0
        if len(to_explore) > 1:
            value_to_add = 1
        new_locations = map(lambda tuple: LocationWithWandMoves(tuple[0], tuple[1], top_location.passes + value_to_add), to_explore)
        for location in new_locations:
            visited[location.i][location.j] = 1
            queue.append(location)

cases = int(input().strip())
for i in range(cases):
    rows, columns = list(map(int, input().strip().split(' ')))
    grid = []
    for grid_i in range(rows):
        grid_t = list(input().strip())
        grid.append(grid_t)
    guesses = int(input())
    if determine_if_impresses(grid, guesses):
        print('Impressed')
    else:
        print('Oops!')




