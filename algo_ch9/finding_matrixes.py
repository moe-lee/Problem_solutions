from collections import deque

def BFS(grid, tr, tc) :
    queue = deque()
    max_row, max_col = tr, tc
    queue.append((tr, tc))
    grid[tr][tc] = 0
    steps = ((1, 0), (0, 1))
    while queue :
        cr, cc = queue.popleft()
        for sr, sc in steps :
            nr, nc = cr+sr, cc+sc
            if(0<=nr<len(grid)) and (0<=nc<len(grid)) and grid[nr][nc] != 0 :
                max_row = max(max_row, nr)
                max_col = max(max_col, nc)
                grid[nr][nc] = 0
                queue.append((nr, nc))
    return (max_row - tr + 1, max_col - tc + 1)


T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    matrixes = []
    for i in range(N) :
        for j in range(N) :
            if grid[i][j] != 0 :
                matrixes.append(BFS(grid, i, j))
    matrixes.sort(key= lambda x : (x[0] * x[1], x[0], x[1]))
    print('#'+str(test_case), len(matrixes), end="")
    for mat in matrixes :
        print(" "+str(mat[0]),mat[1], end="")
    print()