import sys

arr_2d = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

def getZero(arr_2d):
    t_arr = []
    for x in range(9):
        for y in range(9):
            if arr_2d[x][y] == 0:
                t_arr.append((x,y))
    
    return t_arr

def isPossibleNumber(arr_2d_in, x, y, n):
    if n in arr_2d_in[x]:
        return False
    
    for i in range(9):
        if n == arr_2d_in[i][y]:
            return False
    
    idx = x//3*3
    idy = y//3*3
    for t_x in range(idx, idx+3):
        for t_y in range(idy, idy+3):
            if n == arr_2d_in[t_x][t_y]:
                return False
    
    return True

def dfs(n):
    
    if len(zeroXys) == n:
        for x in arr_2d:
            for y in x:
                print(y, end=" ")
            print()

        sys.exit(0)
    
    for i in range(1,10):
        if isPossibleNumber(arr_2d, zeroXys[n][0], zeroXys[n][1], i):
            arr_2d[zeroXys[n][0]][zeroXys[n][1]] = i
            dfs(n+1)
        
        arr_2d[zeroXys[n][0]][zeroXys[n][1]] = 0

zeroXys = getZero(arr_2d)

dfs(0)

arr_2d = [list(map(str, x)) for x in arr_2d]
[print(' '.join(x)) for x in arr_2d]