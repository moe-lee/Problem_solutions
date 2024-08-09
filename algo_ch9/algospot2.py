import sys
import heapq

def solve() :
    M, N = map(int, sys.stdin.readline().split())
    grid = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    pq = [(0, 0, 0)] # 부순 벽 수, row, col
    visited = set()
    visited.add((0 ,0))
    ans = 0
    while pq :
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if(cur_row, cur_col) == (N-1, M-1) :
            ans = cur_cost
            break
        for sr, sc in steps :
            nr, nc = cur_row + sr, cur_col + sc
            if 0<=nr<N and 0<=nc<M and (nr, nc) not in visited :
                heapq.heappush(pq, (cur_cost + grid[nr][nc], nr, nc))
                visited.add((nr, nc))
    print(ans)
solve()