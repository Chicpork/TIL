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

def max_heapify_without_recursion(A, i, heap_size=-1):
    if heap_size < 0:
        heap_size = len(A)

    max_index = i

    while True:
        left = 2*i
        right = left+1

        if left > heap_size:
            break

        if left <= heap_size and A[max_index-1] < A[left-1]:
            max_index = left
        
        if right <= heap_size and A[max_index-1] < A[right-1]:
            max_index = right
        
        if max_index != i:
            A[i-1], A[max_index-1] = A[max_index-1], A[i-1]
            i = max_index
        else:
            break

def build_max_heapify(A):
    for i in range(int(len(A)/2), 0, -1):
        max_heapify_without_recursion(A, i)

def heap_sort(A):
    heap_size = len(A)
    build_max_heapify(A)

    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify_without_recursion(A, 1, heap_size)
    
    return A

def quicksort_partition(A, p, r):
    last = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= last:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quicksort(A, p, r):
    if p < r:
        q = quicksort_partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    
    return A

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
print(quicksort(test_arr, 0, len(test_arr)-1))
print()
print(test_arr)
print(heap_sort(test_arr))