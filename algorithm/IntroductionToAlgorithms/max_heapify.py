A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

def max_heapify(A, i):
    max_index = i
    left = 2*i
    right = left+1
    if left <= len(A) and A[max_index-1] < A[left-1]:
        max_index = left
    
    if right <= len(A) and A[max_index-1] < A[right-1]:
        max_index = right
    
    if max_index != i:
        A[i-1], A[max_index-1] = A[max_index-1], A[i-1]
        max_heapify(A, max_index)

def max_heapify2(A, i):
    max_index = i
    left = 2*(i+1) - 1
    right = left+1
    if left <= len(A) and A[max_index] < A[left]:
        max_index = left
    
    if right <= len(A) and A[max_index] < A[right]:
        max_index = right
    
    if max_index != i:
        A[i], A[max_index] = A[max_index], A[i]
        max_heapify2(A, max_index)

def max_heapify3(A, i):
    index_i = i -1
    max_index = index_i
    left = 2*i - 1
    right = left + 1
    if left < len(A) and A[max_index] < A[left]:
        max_index = left
    
    if right < len(A) and A[max_index] < A[right]:
        max_index = right
    
    if max_index != index_i:
        A[index_i], A[max_index] = A[max_index], A[index_i]
        max_heapify3(A, max_index + 1)

def max_heapify_without_recursion(A, i):
    max_index = i

    while True:
        left = 2*i
        right = left+1

        if left > len(A):
            break

        if left <= len(A) and A[max_index-1] < A[left-1]:
            max_index = left
        
        if right <= len(A) and A[max_index-1] < A[right-1]:
            max_index = right
        
        if max_index != i:
            A[i-1], A[max_index-1] = A[max_index-1], A[i-1]
            i = max_index

def min_heapify(A, i):
    min_index = i
    left = 2*i
    right = left+1
    if left <= len(A) and A[min_index-1] > A[left-1]:
        min_index = left
    
    if right <= len(A) and A[min_index-1] > A[right-1]:
        min_index = right
    
    if min_index != i:
        A[i-1], A[min_index-1] = A[min_index-1], A[i-1]
        min_heapify(A, min_index)

def build_max_heapify(A):
    for i in range(int(len(A)/2), 0, -1):
        max_heapify_without_recursion(A, i)


# max_heapify(A,3) # [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]
# max_heapify2(A,2)
# max_heapify3(A,3)
# max_heapify_without_recursion(A, 3)

# min_heapify(A, 3) # [27, 17, 1, 16, 13, 10, 3, 5, 7, 12, 4, 8, 9, 0]

A = [5 , 3, 17, 10, 84, 19, 6, 22 , 9]
build_max_heapify(A)
print(A)