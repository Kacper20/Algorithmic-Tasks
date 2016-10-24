def get_biggest_region(grid):
    rows = len(grid)
    columns = len(grid[0])

    regions = []
    visited = [[0 for x in range(columns)] for y in range(rows)]

    def dfs(row, column, region_array):
        visited[row][column] = 1
        if grid[row][column] == 1:
            region_array.append((row, column))
        else:
            return
        #Could check visited inside recursive call but wanted to optimise it a bit
        if column - 1 >= 0 and not visited[row][column - 1]:
            dfs(row, column - 1, region_array)
        if column + 1 < columns and not visited[row][column + 1]:
            dfs(row, column + 1, region_array)
        if row - 1 >= 0 and not visited[row - 1][column]:
            dfs(row - 1, column, region_array)
        if row + 1 < rows and not visited[row + 1][column]:
            dfs(row + 1, column, region_array)
        if column - 1 >= 0 and row - 1 >= 0 and not visited[row - 1][column - 1]:
            dfs(row - 1, column - 1, region_array)
        if column + 1 < columns and row + 1 < rows and not visited[row + 1][column + 1]:
            dfs(row + 1, column + 1, region_array)
        if column - 1 >= 0 and row + 1 < rows and not visited[row + 1][column - 1]:
            dfs(row + 1, column - 1, region_array)
        if column + 1 < columns and row - 1 >= 0 and not visited[row - 1][column + 1]:
            dfs(row - 1, column + 1, region_array)

    for row_num in range(rows):
        for col_num in range(columns):
            if visited[row_num][col_num] == 0:
                new_region = []
                dfs(row_num, col_num, new_region)
                regions.append(new_region)
    return len(max(regions, key=lambda arr: len(arr)))

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(get_biggest_region(grid))

