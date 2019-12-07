cnt = int(input())
arr = []
for i in range(cnt):
    arr.append(int(input()))

arr.sort()

[print(x) for x in arr]