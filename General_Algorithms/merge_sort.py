def merge_sort(tab, helper, low, high):
    # Only if we have two or more elements
    if high > low:
        middle = (low + high) / 2
        merge_sort(tab, helper, low, middle)
        merge_sort(tab, helper, middle + 1, high)
        merge(tab, helper, low, middle, high)


def merge(tab, helper, low, middle, high):
    for i in range(low, high + 1):
        helper[i] = tab[i]
    i = low
    j = middle + 1
    k = low
    while i <= middle and j <= high:
        if helper[i] <= helper[j]:
            tab[k] = helper[i]
            i += 1
        else:
            tab[k] = helper[j]
            j += 1
        k += 1
    for temp_i in range(i, middle + 1):
        tab[k] = helper[temp_i]
        k + 1


def merge_sort_array(array):
    merge_sort(array, [0] * len(array), 0, len(array) - 1)


arr = [6, 3, 9, 1, 0, 9, 6, 8]
merge_sort_array(arr)
print(arr)