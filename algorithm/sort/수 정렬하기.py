import sys
cnt = int(input())
arr = []
for i in range(cnt):
    arr.append(int(sys.stdin.readline()))

arr.sort()

[print(x) for x in arr]