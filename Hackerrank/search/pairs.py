N, K = raw_input().split()
diff = int(K)
numbers = map(int, raw_input().split())
counter = 0
s = set(numbers)
for num in s:
    if num+diff in s:
        counter +=1
print counter
    