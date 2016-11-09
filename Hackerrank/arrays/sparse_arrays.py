strings_count = int(input())
dict = dict()
for _ in range(strings_count):
    str = input().strip()
    if str in dict:
        dict[str] += 1
    else:
        dict[str] = 1
queries = int(input())
for _ in range(queries):
    query_string = input().strip()
    if query_string in dict:
        print(dict[query_string])
    else:
        print(0)
        