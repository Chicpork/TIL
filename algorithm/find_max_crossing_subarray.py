# %%
import random
import sys
import time
import matplotlib.pyplot as plt
# %%
def find_max_crossing_subarray(in_arr, low, mid, high):
    left_sum = -sys.maxsize
    max_left = -sys.maxsize
    sum = 0
    for ix in range(mid, low-1, -1):
        sum = sum + in_arr[ix]
        if left_sum < sum:
            left_sum = sum
            max_left = ix

    right_sum = -sys.maxsize
    max_right = -sys.maxsize
    sum = 0
    for ix in range(mid+1, high+1, 1):
        sum = sum + in_arr[ix]
        if right_sum < sum:
            right_sum = sum
            max_right = ix
    
    return (max_left, max_right, left_sum + right_sum)

def find_maxmum_subarray(in_arr, low, high):
    if low == high:
        return (low, high, in_arr[low])
    else:
        mid = int((low+high)/2)
        (left_low, left_high, left_sum) = find_maxmum_subarray(in_arr, low, mid)
        (right_low, right_high, right_sum) = find_maxmum_subarray(in_arr, mid+1, high)
        (center_low, center_high, center_sum) = find_max_crossing_subarray(in_arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= center_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= center_sum:
            return (right_low, right_high, right_sum)
        else:
            return (center_low, center_high, center_sum)

def find_maxmum_subarray_bad(in_arr):
    max = -sys.maxsize
    left = -1
    right = -1
    for i in range(len(in_arr)):
        sum = 0
        for j in range(i, len(in_arr)):
            sum = sum + in_arr[j]
            if max < sum:
                max = sum
                left = i
                right = j
    
    return (left, right, max)

def find_maxmum_subarray_notrecursive(in_arr):
    if len(in_arr) == 1:
        return (0, 0, in_arr[0])
    
    left = 0
    right = 0
    max_sum = in_arr[0]
    for i in range(1, len(in_arr), 1):
        sum = 0
        temp_max_sum = -sys.maxsize
        temp_left = 0
        for j in range(i, right, -1):
            
            sum = sum + in_arr[j]
            if sum > temp_max_sum:
                temp_max_sum = sum
                temp_left = j
        
        if sum > 0:
            right = i
            max_sum = max_sum + sum
        elif sum == 0:
            pass
        else:
            if temp_max_sum > max_sum:
                left = temp_left
                right = i
                max_sum = temp_max_sum
        
    return (left, right, max_sum)

# %%
def find_maxmum_subarray_original(ori_arr):
    if len(ori_arr) < 2:
        return []
    
    left = 0
    right = 0
    min_index = 0
    max_sum = -sys.maxsize

    for i in range(1, len(ori_arr), 1):
        if ori_arr[min_index] >= ori_arr[i]:
            min_index = i
        else:
            if (ori_arr[i] - ori_arr[min_index]) > max_sum:
                left = min_index
                right = i
                min_index = i
                max_sum = ori_arr[right] - ori_arr[left]
        print(left, right, min_index, max_sum)
    
    return (left, right, ori_arr[right] - ori_arr[left])
                    
# %%
# test_arr2 = [10, -100, 1, 2, 7]
# test_arr2 = [18, 20, -7, 12, 13, -3, -25, 20, -3, -16, -23,  -5, -22, 15, -4, 7]
# test_arr2 = [-18, -20, -7, -12, -13, -3, -25, -20, -3, -16, -23,  -5, -22, -15, -4, -7]
# test_arr2 = [-12,-2,-3,-4,-1,-10,-70,-11]
# test_arr2 = [30, 20, 8, 2, 4, 9, 3, 7, 13, 0, 18, 5, 12, 16, 19, 10, 0, 17, 6, 11, 14]
test_arr2 = [30, 20, 8, 2, 4, 10, 0, 11]
# test_arr2 = [0, 100, 5]

print(find_maxmum_subarray(test_arr2, 0, len(test_arr2)-1))
print(find_maxmum_subarray_bad(test_arr2))
print(find_maxmum_subarray_notrecursive(test_arr2))
print(find_maxmum_subarray_original(test_arr2))


# %%
size_x = 100
for n in range(1, size_x, 1):
    test_arr2 = random.sample(range(100), 100)

# %%
t_n = 1 # 테스트를 위해 똑같은 list를 몇번 정렬할지
size_x = 100
x = list(range(1,size_x))
total_good_time = []
total_bad_time = []
total_notrecursive_time = []
result0 = []
result1 = []
result2 = []

for n in range(1, size_x, 1):
    test_arr = random.sample(range(n), n)

    s_time = time.time()
    for i in range(t_n):
        result0.append(find_maxmum_subarray(test_arr, 0, len(test_arr)-1))

    total_good_time.append(time.time() - s_time)

    s_time = time.time()
    for i in range(t_n):
        result1.append(find_maxmum_subarray_bad(test_arr))

    total_bad_time.append(time.time() - s_time)

    s_time = time.time()
    for i in range(t_n):
        result2.append(find_maxmum_subarray_notrecursive(test_arr))
    
    total_notrecursive_time.append(time.time() - s_time)

    if total_good_time[n-1] != total_notrecursive_time[n-1]:
        print(test_arr)
        break

    # if total_good_time[n-1] < total_bad_time[n-1]:
    #     print(n)
    #     break

    # print(n,"------------------------------------")
    # print(n, "total_good_time", total_good_time)
    # print(n, "total_bad_time", total_bad_time)

# %%
plt.plot(x, total_good_time, color='red')
plt.plot(x, total_bad_time, color='blue')
plt.plot(x, total_notrecursive_time, color='green')

plt.xlabel('n')
plt.ylabel('time')

plt.show()

# %%
for n in range(0, len(result0), 1):
    print(n, result0[n] == result1[n], result0[n] == result2[n], result1[n] == result2[n], result0[n], result1[n], result2[n])

# %%
print(result0[1])
print(result1[1])