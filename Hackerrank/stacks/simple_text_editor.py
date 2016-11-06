t = int(input().strip())

history = [""]
for a0 in range(t):
	values = list(input().strip().split())
	command = int(values[0])
	if command == 1:
		history.append(history[-1] + values[1])
	elif command == 2:
		elems_to_delete = int(values[1])
		history.append(history[-1][:-elems_to_delete])
	elif command == 3:
		print(history[-1][int(values[1]) - 1])
	elif command == 4:
		history.pop()
	
