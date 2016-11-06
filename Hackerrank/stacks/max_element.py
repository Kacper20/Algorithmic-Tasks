
t = int(input().strip())
stack = []
max_val = 0
for a0 in range(t):
	values = list(map(int, input().strip().split()))
	if values[0] == 1:
		element = values[1]
		stack.append(element)
		if element > max_val:
			max_val = element
	if values[0] == 2:
		value_removed = stack.pop()				
		if len(stack) == 0:
			max_val = 0
		else:
			max_val = max(stack)
	if values[0] == 3:
		print(max_val)
