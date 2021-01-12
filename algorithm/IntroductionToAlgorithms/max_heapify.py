A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

def max_heapify(A, i):
    max_index = i
    left = 2*i
    right = left+1
    if left <= len(A) and A[max_index-1] <= A[left-1]:
        max_index = left
    
    if right <= len(A) and A[max_index-1] <= A[right-1]:
        max_index = right
    
    if max_index != i:
        A[i-1], A[max_index-1] = A[max_index-1], A[i-1]
        print(max_index, A)
        max_heapify(A, max_index)

def max_heapify2(A, i):
    max_index = i
    left = 2*(i+1) - 1
    right = left+1
    if left <= len(A) and A[max_index] <= A[left]:
        max_index = left
    
    if right <= len(A) and A[max_index] <= A[right]:
        max_index = right
    
    if max_index != i:
        A[i], A[max_index] = A[max_index], A[i]
        print(max_index, A)
        max_heapify2(A, max_index)

def max_heapify3(A, i):
    index_i = i -1
    max_index = index_i
    left = 2*i - 1
    right = left + 1
    if left < len(A) and A[max_index] <= A[left]:
        max_index = left
    
    if right < len(A) and A[max_index] <= A[right]:
        max_index = right
    
    if max_index != index_i:
        A[index_i], A[max_index] = A[max_index], A[index_i]
        print(max_index, A)
        max_heapify3(A, max_index + 1)
    
# max_heapify(A,3)
# max_heapify2(A,2)
max_heapify3(A,3)
print(A)

# [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]