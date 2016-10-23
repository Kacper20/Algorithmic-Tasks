class MyQueue(object):
	def __init__(self):
		self.left = []
		self.right = []
	
	def peek(self):
		if len(self.left) == 0:
			self.right.reverse()
			self.left = self.right
			self.right = []
		return self.left[-1]	
		
	def pop(self):
		val_to_return = self.peek()
		del(self.left[-1])
		return val_to_return

		
	def put(self, value):
		self.right.append(value)
	
queue = MyQueue()

t = int(input())
for line in range(t):
	values = map(int, input().split())
	values = list(values)
	if values[0] == 1:
		queue.put(values[1])
	elif values[0] == 2:
		queue.pop()
	else:
		print(queue.peek())

