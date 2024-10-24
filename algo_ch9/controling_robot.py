import sys
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, M) : grid[0][i] += grid[0][i-1]
for i in range(1, N) :
    lefts = grid[i][:]
    rights = grid[i][:]
    for j in range(0, M) :
        if j == 0 : lefts[j] += grid[i-1][j]
        else : lefts[j] += max(grid[i-1][j], lefts[j-1])
    for j in range(M-1, -1, -1) :
        if j == M-1 : rights[j] += grid[i-1][j]
        else : rights[j] += max(grid[i-1][j], rights[j+1])
    for j in range(0, M) :
        grid[i][j] = max(lefts[j], rights[j])
print(grid[N-1][M-1])