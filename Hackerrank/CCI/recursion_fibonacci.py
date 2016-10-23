memoization = dict()
def fibonacci(n):
	if n == 0 or n == 1:
		return n
	minusOne = None
	if (n-1) in memoization:
		minusOne = memoization[n-1]
	else:
		minusOne = fibonacci(n-1)
		memoization[n-1] = minusOne
	minusTwo = None
	if (n-2) in memoization:
		minusTwo = memoization[n-2]
	else:
		minusTwo = fibonacci(n-2)
		memoization[n-2] = minusTwo
	return minusOne + minusTwo
n = int(input())
print(fibonacci(n))
