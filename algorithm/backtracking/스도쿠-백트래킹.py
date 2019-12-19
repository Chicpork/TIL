import sys
import copy

arr_2d = [list(map(int,sys.stdin.readline().split())) for i in range(9)]
isFound = False

def isPossibleNumber(arr_2d_in, x, y, n):
    if n in arr_2d_in[x]:
        return False
    
    for i in range(9):
        if n == arr_2d_in[i][y]:
            return False
    
    idx = int(x/3)*3
    idy = int(y/3)*3
    for t_x in range(idx, idx+3):
        for t_y in range(idy, idy+3):
            if n == arr_2d_in[t_x][t_y]:
                return False
    
    return True

def getZero(arr_2d):
    t_arr = []
    for x in range(9):
        for y in range(9):
            if arr_2d[x][y] == 0:
                t_arr.append((x,y))
    
    return t_arr

def dfs(arr_2d_in, zeroXys, n):
    global arr_2d
    global isFound
    
    if len(zeroXys) == n:
        arr_2d = arr_2d_in
        isFound = True
        return
    
    for i in range(1,10):
        if isPossibleNumber(arr_2d_in, zeroXys[n][0], zeroXys[n][1], i):
            t_arr_2d_in = copy.deepcopy(arr_2d_in)
            t_arr_2d_in[zeroXys[n][0]][zeroXys[n][1]] = i
            dfs(t_arr_2d_in, zeroXys, n+1)
        
        if isFound:
            return

zeroXys = getZero(arr_2d)

dfs(arr_2d, zeroXys, 0)

arr_2d = [list(map(str, x)) for x in arr_2d]
[print(' '.join(x)) for x in arr_2d]