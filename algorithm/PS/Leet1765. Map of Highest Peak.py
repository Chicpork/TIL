# %%
from collections import deque

def highestPeak(isWater):
    q = deque()
    height = [[-1]*len(isWater[0]) for _ in range(len(isWater))]
    for ix, row in enumerate(isWater):
        for iy, val in enumerate(row):
            if val == 1:
                q.append((ix,iy))
                height[ix][iy] = 0

    while q:
        x, y = q.popleft()
        h = height[x][y]
        
        if x-1 >= 0 and height[x-1][y] < 0:
            q.append((x-1,y))
            height[x-1][y] = h + 1
        
        if x+1 < len(height) and height[x+1][y] < 0:
            q.append((x+1,y))
            height[x+1][y] = h + 1
        
        if y-1 >= 0 and height[x][y-1] < 0:
            q.append((x,y-1))
            height[x][y-1] = h + 1
        
        if y+1 < len(height[x]) and height[x][y+1] < 0:
            q.append((x,y+1))
            height[x][y+1] = h + 1

    return height


print(highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
