N = int(input())
cnt = 0

def check(arr_in, n, i):
    for j in range(n):
        if abs(arr_in[j] - i) == abs(j - n):
            return False

    return True

def set_queen(arr_in, remain_rows, n):
    global cnt
    if n >= N :
        # print(arr_in)
        cnt += 1
        return

    # 첫번째 열부터 마지막 행까지 돌면서 확인
    for i in remain_rows:
        if check(arr_in, n, i):
            arr_in[n] = i
            temp_remain_rows = remain_rows.copy()
            temp_remain_rows.remove(i)
            set_queen(arr_in, temp_remain_rows, n + 1)
    
    return

if N == 1:
    print(1)
else:    
    for i in range(int(N/2)):
        arr = [0]*N
        arr[0] = i
        remain_rows = set(range(N))
        remain_rows.remove(arr[0])
        set_queen(arr, remain_rows, 1)

    cnt *= 2

    if N%2 == 1:
        arr = [0]*N
        arr[0] = (N-1)/2
        remain_rows = set(range(N))
        remain_rows.remove(arr[0])
        set_queen(arr, remain_rows, 1)

    print(cnt)