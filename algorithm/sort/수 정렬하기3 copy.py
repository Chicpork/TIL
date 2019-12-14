import time

start = time.time()  # 시작 시간 저장

f = open("C:/develop/TIL/algorithm/sort/test.txt", "r")

arr = [0] * 10001

stt1 = time.time()
cnt = int(f.readline())
for i in range(cnt):
    arr[int(f.readline())] += 1

edt = time.time()
print("time 1 :", edt - stt1)  # 현재시각 - 시작시간 = 실행 시간
# cnt = int(input())
# for i in range(cnt):
#     arr[int(input())] += 1

# for k in range(1000):
#     for i, item in enumerate(arr):
#         for j in range(item):
#             print(i)

stt1 = time.time()
output = []

for i, item in enumerate(arr):
    output += [''.join([str(i), '\n']) for j in range(item)]

output = ''.join(output)

edt = time.time()
print("time 1 :", edt - stt1)  # 현재시각 - 시작시간 = 실행 시간
# print(output[:-1])

end = time.time() # 종료 시간

print("time :", end - start)  # 현재시각 - 시작시간 = 실행 시간