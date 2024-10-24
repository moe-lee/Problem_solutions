import sys
import heapq
# Dijkstra 알고리즘을 모든 점에 대해서 수행
# 0,0 에서 출발해 [i,j] 까지 가는 최소 비용 + [i,j]에서 0,0 으로 최소비용 <= D 인 최댓값 grid[i,j]
def dijkstra(grid, init_row, init_col, to_set, T, D, N, M) :
    costs = {}
    pq = [(0, init_row, init_col)]
    step = ((-1, 0), (0, -1), (1, 0), (0, 1))
    while pq :
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if (cur_row, cur_col) not in costs :
            costs[(cur_row, cur_col)] = cur_cost
            if (cur_row, cur_col) in to_set : return costs
            for sr, sc in step :
                nr, nc = cur_row + sr, cur_col + sc
                if(0<=nr<N) and (0<=nc<M) and (nr,nc) not in costs and abs(grid[cur_row][cur_col] - grid[nr][nc]) <= T:
                    next_cost = cur_cost + (1 if grid[cur_row][cur_col] >= grid[nr][nc] else (grid[nr][nc] - grid[cur_row][cur_col]) ** 2)
                    if next_cost < D :
                        heapq.heappush(pq, (next_cost, nr, nc))
    return costs

def alphaToInt(s) :
    c = ord(s)
    a = c & 0x1F
    if(c & 0x20) : a+= 26
    return a - 1

def solve() :
    N, M, T, D = map(int, sys.stdin.readline().split())
    
    grid = [list(map(alphaToInt, list(sys.stdin.readline().strip()))) for _ in range(N)]
    costs = [[None for _ in range(M)] for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            to_set = {(0, 0)}
            if (i, j) == (0, 0) : to_set = set()
            costs[i][j] = dijkstra(grid, i, j, to_set, T, D, N, M)
    max_height = 0
    for i in range(N) :
        for j in range(M) :
            if (i, j) in costs[0][0] and (0, 0) in costs[i][j] :
                if costs[0][0][(i,j)] + costs[i][j][(0,0)] <= D :
                    max_height = max(max_height, grid[i][j])
    print(max_height)
solve()

'''
2 2 1 1
B a
a a
'''