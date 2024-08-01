
def uniquePaths(m, n) :
    grid = [[0 for _ in range(n)] for _ in range(m)]
    grid[0][0] = 1
    for i in range(m) :
        for j in range(n) :
            if i == j and i == 0 : continue
            from_top = grid[i-1][j] if (i > 0) else 0
            from_left = grid[i][j-1] if (j > 0) else 0
            grid[i][j] = from_top + from_left
    return grid[m-1][n-1]

print(uniquePaths(m=3,n=2))