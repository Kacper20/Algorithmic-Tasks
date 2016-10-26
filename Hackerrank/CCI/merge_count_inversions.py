def merge_sort(tab, helper, low, high):
    # Only if we have two or more elements
    if high > low:
        middle = int((low + high) / 2)
        inversion_count = merge_sort(tab, helper, low, middle)
        inversion_count += merge_sort(tab, helper, middle + 1, high)
        inversion_count += merge(tab, helper, low, middle, high)
        return inversion_count
    return 0


def merge(tab, helper, low, middle, high):
    inversion_count = 0
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
            inversion_count += (middle - i + 1)
            tab[k] = helper[j]
            j += 1
        k += 1
    for temp_i in range(i, middle + 1):
        tab[k] = helper[temp_i]
        k += 1
    return inversion_count

def count_inversions(a):
    return merge_sort(a, [0] * len(a), 0, len(a) - 1)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))

