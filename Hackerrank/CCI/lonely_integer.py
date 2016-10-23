import sys

def lonely_integer(a):
    result = 0
    for num in a:
        result ^= num
    return result

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
