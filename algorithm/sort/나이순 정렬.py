import sys

cnt = int(input())
arr_2d = [[i] + sys.stdin.readline().split() for i in range(cnt)]

[print(x[1], x[2]) for x in sorted(arr_2d, key=lambda x: (int(x[1]),x[0]))]