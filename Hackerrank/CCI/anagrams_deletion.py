import sys

def anagrams_deletions(first, second):
	dictionary = dict()
	for x in first:
		if not x in dictionary:
			dictionary[x] = -1
		else:
			dictionary[x] -= 1
	for y in second:
		if not y in dictionary:
			dictionary[y] = 1
		else:
			dictionary[y] += 1
	counter = 0
	for value in dictionary:
		counter += abs(dictionary[value])
	print(counter)
def compute():
	anagram_1 = sys.stdin.readline().strip()
	anagram_2 = sys.stdin.readline().strip()
	anagrams_deletions(anagram_1, anagram_2)

compute()
