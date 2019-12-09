import sys

cnt = int(input())
lists = set()
[lists.add(sys.stdin.readline().rstrip()) for x in range(cnt)]

[print(x) for x in sorted(lists, key=lambda x: (len(x), x))]