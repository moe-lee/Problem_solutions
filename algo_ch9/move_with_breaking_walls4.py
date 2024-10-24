import sys
from collections import deque

def BFS(grid, visited, N, M, row, col) :
    step = ((-1, 0), (1, 0), (0, -1), (0, 1))
    queue = deque()
    queue.append((row, col))
    zeros = 0
    walls = set()
    visited[row][col] = True
    while queue :
        cr, cc = queue.popleft()
        zeros += 1
        for sr, sc in step :
            nr, nc = cr + sr, cc + sc
            if (0<=nr<N)and(0<=nc<M) :
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    queue.append((nr,nc))
                    visited[nr][nc] = True
                elif grid[nr][nc] != 0 and (nr,nc) not in walls:
                    walls.add((nr,nc))
    for cr, cc in walls : grid[cr][cc] += zeros

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 0 and not visited[i][j] :
                BFS(grid=grid,visited=visited,N=N,M=M,row=i,col=j)
    for i in range(N) :
        for j in range(M) :
            print(grid[i][j] % 10, end="")
        print()
solve()