import sys
from collections import deque
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    ans = 0
    def BFS(row, col) :
        queue = deque()
        queue.append((row, col, 0))
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[row][col] = True
        steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
        max_dist = 0
        while queue :
            cr, cc, cd = queue.popleft()
            max_dist = max(max_dist, cd)
            for sr, sc in steps :
                nr, nc, nd = cr + sr, cc + sc, cd + 1
                if (0<=nr<N and 0<=nc<M) and not visited[nr][nc] and grid[nr][nc] == 'L' :
                    visited[nr][nc] = True
                    queue.append((nr, nc, nd))
        return max_dist

    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 'L' :
                ans = max(ans, BFS(i, j))
    print(ans)
solve()