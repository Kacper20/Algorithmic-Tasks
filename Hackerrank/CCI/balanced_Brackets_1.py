def is_matched(expression):
		bracket_stack = []
		opening_brackets = ["[", "{", "("]
		closing_brackets = ["]", "}", ")"]
		
		for bracket in expression:
			if bracket in opening_brackets:
				bracket_stack.append(bracket)
			if bracket in closing_brackets:
				if len(bracket_stack) == 0 or not are_parentheses_in_pair(bracket_stack[-1], bracket):
						return False
				else:
					bracket_stack = bracket_stack[:-1]
		return len(bracket_stack) == 0
		
def are_parentheses_in_pair(a, b):
	return a == "(" and b == ")" or a == "[" and b == "]" or a == "{" and b == "}"

t = int(input().strip())
for a0 in range(t):
		expression = input().strip()
		if is_matched(expression) == True:
				print("YES")
		else:
				print("NO")
