import sys
import heapq

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    start = None
    finish = None
    step = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    garbage_point = [[0 for _ in range(M)] for _ in range(N)]
    garbage_adj = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 'S' : start = (i, j)
            elif grid[i][j] == 'F' : finish = (i, j)
            elif grid[i][j] == 'g' :
                garbage_point[i][j] = 1
                for sr, sc in step :
                    nr, nc = i + sr, j + sc
                    if (0 <= nr < N) and (0 <= nc < M) and grid[nr][nc] != 'S' and grid[nr][nc] != 'F':
                        garbage_adj[nr][nc] = 1
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    pq = [(garbage_point[start[0]][start[1]], garbage_adj[start[0]][start[1]], start[0], start[1])]
    while pq :
        gc, agc, cr, cc = heapq.heappop(pq)
        if not visited[cr][cc] :
            visited[cr][cc] = (gc, agc)
            for sr, sc in step :
                nr, nc, ngc, nagc = cr + sr, cc + sc, gc, agc
                if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc]:
                    if grid[nr][nc] == 'g' : ngc = gc + garbage_point[nr][nc]
                    else : nagc =  agc +garbage_adj[nr][nc]
                    heapq.heappush(pq, (ngc, nagc, nr, nc))
    
    print(*visited[finish[0]][finish[1]])
solve()


'''
5 3
..F
.gg
..g
..g
..S
ans = 0 2

5 3
..F
ggg
..g
..g
..S
ans = 1 3

6 5
..F..
.....
.g.gg
.....
.....
....S
ans = 0 1

3 3
ggF
ggg
Sgg
ans = 3 0

3 3
ggg
SgF
...
ans = 0 1

5 5
ggggg
ggFgg
.ggg.
.....
....S

'''
