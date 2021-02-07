import time
import random
import copy

def burble_sort(in_arr):
    n = len(in_arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if in_arr[j] > in_arr[j+1]:
                in_arr[j], in_arr[j+1] = in_arr[j+1], in_arr[j]
    
    return in_arr

def selection_sort(in_arr):
    n = len(in_arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n, 1):
            if in_arr[min_idx] > in_arr[j]:
                min_idx = j
        in_arr[i], in_arr[min_idx] = in_arr[min_idx], in_arr[i]
    
    return in_arr

def selection_sort2(in_arr):
    n = len(in_arr)
    for i in range(int((n+1)/2)):
        min_idx = i
        max_idx = i
        for j in range(i+1, n, 1):
            if in_arr[min_idx] > in_arr[j]:
                min_idx = j
            elif in_arr[max_idx] < in_arr[j]:
                max_idx = j
        print(i,j,min_idx,max_idx)
        in_arr[i], in_arr[min_idx] = in_arr[min_idx], in_arr[i]
        if i != j:
            in_arr[n-i-1], in_arr[max_idx] = in_arr[max_idx], in_arr[n-i-1]
    
    return in_arr

def insertion_sort(in_arr):
    n = len(in_arr)
    for i in range(1, n, 1):
        for j in range(i, 0, -1):
            if in_arr[j] < in_arr[j-1]:
                in_arr[j-1], in_arr[j] = in_arr[j], in_arr[j-1]
            else:
                break
        
    return in_arr

def quick_sort(in_arr):
    if len(in_arr) <= 1:
        return in_arr
    left = [x for x in in_arr[1:] if x < in_arr[0]]
    right = [x for x in in_arr[1:] if x >= in_arr[0]]

    return quick_sort(left) + [in_arr[0]] + quick_sort(right)

def merge_sort(in_arr):
    return split(in_arr)

def split(list):
    if len(list) == 1:
        return list
    
    left = list[:int((len(list)+1)/2)]
    right = list[int((len(list)+1)/2):]
    
    return merge(split(left), split(right))

def merge(left, right):
    out_list = []
    
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            out_list.append(right.pop(0))
        else:
            out_list.append(left.pop(0))
    
    out_list = out_list + left + right
    return out_list

n = 10 # size of random array
test_arr = random.sample(range(n), n)
#print(test_arr)

# s_time = time.time()
# burble_sort(copy.deepcopy(test_arr))
# print("time : ",time.time() - s_time)
# s_time = time.time()
# selection_sort(copy.deepcopy(test_arr))
# print("time : ",time.time() - s_time)
# s_time = time.time()
# insertion_sort(copy.deepcopy(test_arr))
# print("time : ",time.time() - s_time)

# print(selection_sort2([3,5,6,4,2,1]))
print(test_arr)
print(quick_sort(test_arr))
print()
print(test_arr)
print(merge_sort(test_arr))
print()
print(test_arr)
print(heap_sort(test_arr))
print()
test_arr = [13, 19, 9, 5 , 12 , 8 , 7, 4 , 21 , 2 , 6, 11]
print(test_arr)
print(quicksort(test_arr, 0, len(test_arr)-1))

print(quicksort_partition([1,1,1], 0, 2))