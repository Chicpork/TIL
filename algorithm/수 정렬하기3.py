import time
start = time.time()  # 시작 시간 저장

arr = [0] * 10001
cnt = int(input())
for i in range(cnt):
    arr[int(input())] += 1

for k in range(1000):
    for i, item in enumerate(arr):
        for j in range(item):
            print(i)
# output = []
# for k in range(1000):
#     for i, item in enumerate(arr):
#         output += [''.join([str(i), '\n']) for j in range(item)]

# output = ''.join(output)

# print(output[:-1])

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간