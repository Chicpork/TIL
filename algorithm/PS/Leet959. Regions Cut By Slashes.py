def regionsBySlashes(grid):
    grid_visit_yn = [[[False, False, False, False] for _ in range(len(grid))] for _ in range(len(grid))]
    
    def dfs(i, j, location):
        grid_visit_yn[i][j][location] = True
        
        if location == 0:
            if grid[i][j] != '\\' and not grid_visit_yn[i][j][3]:
                dfs(i, j, 3)
            if grid[i][j] != '/' and not grid_visit_yn[i][j][1]:
                dfs(i, j, 1)
            if i-1 >= 0 and not grid_visit_yn[i-1][j][2]:
                dfs(i-1, j, 2)
        elif location == 1:
            if grid[i][j] != '\\' and not grid_visit_yn[i][j][2]:
                dfs(i, j, 2)
            if grid[i][j] != '/' and not grid_visit_yn[i][j][0]:
                dfs(i, j, 0)
            if j+1 < len(grid) and not grid_visit_yn[i][j+1][3]:
                dfs(i, j+1, 3)
        elif location == 2:
            if grid[i][j] != '\\' and not grid_visit_yn[i][j][1]:
                dfs(i, j, 1)
            if grid[i][j] != '/' and not grid_visit_yn[i][j][3]:
                dfs(i, j, 3)
            if i+1 < len(grid) and not grid_visit_yn[i+1][j][0]:
                dfs(i+1, j, 0)
        elif location == 3:
            if grid[i][j] != '\\' and not grid_visit_yn[i][j][0]:
                dfs(i, j, 0)
            if grid[i][j] != '/' and not grid_visit_yn[i][j][2]:
                dfs(i, j, 2)
            if j-1 >= 0 and not grid_visit_yn[i][j-1][1]:
                dfs(i, j-1, 1)
    
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for location in range(4):
                if not grid_visit_yn[i][j][location]:
                    cnt += 1
                    dfs(i, j, location)
    
    return cnt


print(regionsBySlashes(
[
  "/\\",
  "\\/"
]
))