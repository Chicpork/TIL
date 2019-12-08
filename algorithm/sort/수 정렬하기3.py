import sys

arr = [0] * 10001

cnt = int(input())
for i in range(cnt):
    arr[int(sys.stdin.readline())] += 1

for i, item in enumerate(arr):
    for j in range(item):
        print(i)