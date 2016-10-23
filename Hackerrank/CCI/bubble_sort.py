n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

num_of_swaps = 0
for i in range(0, len(a)):
	local_num_of_swaps = 0
	for j in range (0, len(a) - 1):
		if a[j] > a[j+1]:
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
			local_num_of_swaps += 1
	if local_num_of_swaps == 0:
		break
	num_of_swaps += local_num_of_swaps
print('Array is sorted in', num_of_swaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])

