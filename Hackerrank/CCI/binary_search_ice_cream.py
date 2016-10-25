def helper(goal, low, high, array):
    if high < low:
        return -1
    middle = int((low + high) / 2)
    if array[middle] == goal:
        return middle
    elif array[middle] < goal:
        return helper(goal, middle + 1, high, array)
    else:
        return helper(goal, low, middle - 1, array)

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    a_with_indices = [pair for pair in enumerate(a)]
    sorted_array = sorted(a_with_indices, key=lambda pair: pair[1])
    sorted_without_indices = list(map(lambda pair: pair[1], sorted_array))

    def print_results(current_index, other_index, sorted_array):
        first = sorted_array[other_index][0] + 1
        second = sorted_array[current_index][0] + 1
        print(min(first, second), max(first, second))

    for i in range(len(sorted_array)):
        leftover = m - sorted_without_indices[i]
        if leftover <= 0:
            continue
        if leftover <= sorted_without_indices[i]:
            left_search_result = helper(leftover, 0, i - 1, sorted_without_indices)
            if left_search_result != -1:
                print_results(i, left_search_result, sorted_array)
                break
        if leftover >= sorted_without_indices[i]:
            right_search_result = helper(leftover, i + 1, len(sorted_without_indices) - 1, sorted_without_indices)
            if right_search_result != -1:
                print_results(i, right_search_result, sorted_array)
                break




