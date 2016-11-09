len = int(input())
numbers = map(int, input().split())
temp = 0
for number in numbers:
    temp ^= number
print(temp)