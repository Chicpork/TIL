import sys

cnt = int(input())
arr_2d = [list(map(int, sys.stdin.readline().rstrip().split())) for x in range(cnt)]
[print(x[0], x[1]) for x in sorted(arr_2d, key=lambda x: (x[1],x[0]))]