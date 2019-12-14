import sys

cnt = int(input())
arr_2d = [list(map(int, sys.stdin.readline().rstrip().split())) for x in range(cnt)]
[print(x[0], x[1]) for x in sorted(sorted(arr_2d, key=lambda x: x[1]))]


# cnt = cnt - 1
# idx = 0
# idx2 = 0
# while idx < cnt:
#     for i in range(idx,cnt+1):
#         if arr_2d[idx][0] < arr_2d[i][0]:
#             idx2 = i
#             break
#         if i == cnt:
#             idx2 = i
#             break
    

#     arr_2d[idx:idx2] = sorted(arr_2d[idx:idx2], key=lambda x: x[1])
#     idx = idx2

# [print(x[0], x[1]) for x in arr_2d]

# sorted_output = []

# for i in range(cnt):
#     in_2d = sys.stdin.readline().split()
#     is_inserted = False
#     for idx, xy in enumerate(sorted_output):
#         if xy[0] > in_2d[0]:
#             sorted_output.insert(idx, in_2d)
#             is_inserted = True
#         elif xy[0] == in_2d[0]:
#             for idy, xy2 in enumerate(sorted_output[idx:]):
#                 if xy2[0] > in_2d[0]:
#                     sorted_output.insert(idx+idy, in_2d)
#                     is_inserted = True
#                     break

#                 if xy2[1] >= in_2d[1]:
#                     sorted_output.insert(idx+idy, in_2d)
#                     is_inserted = True
#                     break
        
#         if is_inserted:
#             break
        
#     if is_inserted == False:
#         sorted_output.append(in_2d)

# [print(x[0], x[1]) for x in sorted_output]


