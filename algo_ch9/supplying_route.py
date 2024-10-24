import heapq
T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    grid = [list(map(int, list(input()))) for _ in range(N)]
    UNVISITED = -1
    visited = [[UNVISITED for _ in range(N)] for _ in range(N)]
    
    pq = [(0, 0, 0)]
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while pq :
        cd, cr, cc = heapq.heappop(pq)
        if visited[cr][cc] == UNVISITED :
            visited[cr][cc] = cd
            if(cr, cc) == (N-1, N-1) :
                break
            for sr, sc in steps :
                nr, nc = cr + sr, cc + sc
                if(0<= nr < N and 0<= nc <N) and visited[nr][nc] == UNVISITED :
                    heapq.heappush(pq, (cd + grid[nr][nc], nr, nc))
    print('#'+str(test_case), visited[N-1][N-1])