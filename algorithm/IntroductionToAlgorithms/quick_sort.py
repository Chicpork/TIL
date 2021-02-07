import random

def quicksort_partition(A, p, r):
    last = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= last:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    i += 1
    A[i], A[r] = A[r], A[i]

    # i가 r과 같다면 Divide and conquer 가 제대로 되지 않고 한쪽 방향으로만 sorting 이루어짐
    if i == r:
        i = (p + r)//2
    return i

def randomized_quicksort_partition(A, p, r):
    rand_r = random.randrange(p, r)
    A[r], A[rand_r] = A[rand_r], A[r]

    last = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= last:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    i += 1
    A[i], A[r] = A[r], A[i]

    # i가 r과 같다면 Divide and conquer 가 제대로 되지 않고 한쪽 방향으로만 sorting 이루어짐
    if i == r:
        i = (p + r)//2
    return i

def quick_sort(A, p, r):
    if p < r:
        # q = quicksort_partition(A, p, r)
        q = randomized_quicksort_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
    
    return A