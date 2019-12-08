import sys

arr = [0] * 8001

tot_cnt = int(input())
for i in range(tot_cnt):
    arr[int(sys.stdin.readline())+4000] += 1

sum_num = 0
average_num = 0
median_num = 0
mode_num = 0
mode_cnt = 0
mode_dup_cnt = 0
min_num = 4000
max_num = -4000
count = 0
for num, cnt in enumerate(arr):
    num -= 4000

    if cnt > 0:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

        if mode_cnt == cnt and mode_dup_cnt <= 1:
            mode_num = num
            mode_dup_cnt += 1
        elif mode_cnt < cnt:
            mode_num = num
            mode_cnt = cnt
            mode_dup_cnt = 1

        if count < tot_cnt/2:
            median_num = num

        count += cnt

        sum_num += num*cnt

print(int(round(sum_num / tot_cnt, 0)))
print(median_num)
print(mode_num)
print(max_num - min_num)