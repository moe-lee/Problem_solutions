import sys

def solve() :
    N = int(sys.stdin.readline())
    i_grid = []
    for _ in range(N) :
        i_grid.append(list(map(int, sys.stdin.readline().split())))
    
    grid = [[[0,0,0] for _ in range(N)] for _ in range(N)]
    grid[0][1][0] = 1
    for i in range(N) :
        for j in range(2, N) :
            # 0 : 가로 밀기, 1 : 대각선 밀기, 2 : 세로 밀기
            if i_grid[i][j] == 1 : continue
            if j > 0 and i_grid[i][j-1] != 1: grid[i][j][0] = grid[i][j-1][0] + grid[i][j-1][1]
            if i > 0 and j > 0 and (i_grid[i][j-1] != 1 and i_grid[i-1][j] != 1 and i_grid[i-1][j-1] != 1):
                grid[i][j][1] = sum(grid[i-1][j-1])
            if i > 0 and i_grid[i-1][j] != 1 : grid[i][j][2] = grid[i-1][j][1] + grid[i-1][j][2]
    
    print(sum(grid[N-1][N-1]))

solve()