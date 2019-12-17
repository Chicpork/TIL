N = int(input())
cnt = 0

def check(arr_in, n, i):
    for j in range(n):
        if arr_in[j] == i:
            return False
        elif abs(arr_in[j] - i) == abs(j - n):
            return False
    
    return True

def set_queen(arr_in, n, cnt):
    if n >= N :
        # print(arr_in)
        cnt += 1
        return cnt

    for i in range(N):
        if check(arr_in, n, i):
            arr_in[n] = i
            cnt = set_queen(arr_in, n + 1, cnt)
    
    return cnt

for i in range(int(N/2)):
    arr = [0]*N
    arr[0] = i
    cnt += set_queen(arr, 1, 0)

cnt *= 2

if N%2 == 1:
    arr = [0]*N
    arr[0] = (N+1)/2
    cnt + set_queen(arr, 1, cnt)

print(cnt)