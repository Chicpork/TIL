N = int(input())
cnt = 0

def check(arr_in, n, i):
    for j in range(n):
        if arr_in[j] == i:
            return False
        elif abs(arr_in[j] - i) == abs(j - n):
            return False
    
    return True

def set_queen(arr_in, n):
    global cnt
    if n >= N :
        # print(arr_in)
        cnt += 1
        return 

    for i in range(N):
        if check(arr_in, n, i):
            arr_in[n] = i
            set_queen(arr_in, n + 1)
    
    return

for i in range(N):
    arr = [0]*N
    arr[0] = i
    set_queen(arr, 1)

print(cnt)