import sys

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())
max = 0
for i in range (l, r+1):
    for j in range (l, r+1):
        if i ^ j > max:
            max = i ^ j
print max


