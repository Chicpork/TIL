import sys

arr_2d = [list(map(int,sys.stdin.readline().split())) for i in range(9)]

def getPossibleNumber(x, y):
    oneToNine = set(range(1,10))
    rowCheck = set(arr_2d[x])
    colCheck = set()
    for i in range(9):
        colCheck.add(arr_2d[i][y])
    
    oneToNine.difference_update(rowCheck)
    oneToNine.difference_update(colCheck)

    idx = int(x/3)*3
    idy = int(y/3)*3
    for t_x in range(idx, idx+3):
        for t_y in range(idy, idy+3):
            if arr_2d[t_x][t_y] in oneToNine:
                oneToNine.remove(arr_2d[t_x][t_y])
    
    if len(oneToNine) == 1:
        return oneToNine.pop()
    else:
        return 0

cnt = 0
index = 0

while 1:
    if index == 81:
        index = 0
    cnt += 1
    ix = index % 9
    iy = int(index / 9)
    if arr_2d[ix][iy] == 0:
        isOne = getPossibleNumber(ix, iy)
        if isOne != 0:
            arr_2d[ix][iy] = isOne

        cnt = 0
    else:
        cnt += 1

    index += 1
    
    if cnt == 80:
        break

arr_2d = [list(map(str, x)) for x in arr_2d]
[print(' '.join(x)) for x in arr_2d]