import sys
from collections import deque

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    parent = [i for i in range(8)] # 섬은 2번부터 시작
    steps = ((-1, 0),(1, 0), (0, -1), (0, 1))
    def find(x) :
        if x != parent[x] :
            parent[x] = find(parent[x])
            return parent[x]
        return x
    
    def union(x, y) :
        parent[find(y)] = find(x)
    
    def searchEdges(x, y, visited, edges, i_num) :
        # x, y는 시작 노드
        queue = deque()
        queue.append((x, y))
        grid[x][y] = i_num
        visited[x][y] = True
        adj_sea = deque()
        while queue :
            cr, cc = queue.popleft()
            for i in range(len(steps)) :
                nr, nc = cr + steps[i][0], cc + steps[i][1]
                if (0<=nr<N) and (0<=nc<M) :
                    if not visited[nr][nc] and grid[nr][nc]  == 1 :
                        visited[nr][nc] = True
                        grid[nr][nc] = i_num
                        queue.append((nr, nc))
                    if grid[nr][nc] == 0 :
                        adj_sea.append((nr, nc, i, 0, (nr, nc)))
        while adj_sea :
            cr, cc, cd, cost, from_pos = adj_sea.popleft()
            nr, nc, ncost = cr + steps[cd][0], cc + steps[cd][1], cost + 1
            if (0<=nr<N) and (0<=nc<M) :
                if grid[nr][nc] == 1 and ncost > 1 :
                    edges.append([i_num, (nr, nc), ncost])
                elif grid[nr][nc] == 0 :
                    adj_sea.append((nr, nc, cd, ncost, from_pos))
        
    edges = [] # edge => from , to, cost, from_idx, to_idx
    num_of_islands = 2
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M) :
            if grid[i][j] == 1 and not visited[i][j]:
                searchEdges(i, j, visited, edges, num_of_islands)
                num_of_islands += 1
    num_of_groups = num_of_islands - 2
    edges.sort(key=lambda x : -1 * x[2]) # Cost 기준으로 sorting
    tot_cost = 0
    while num_of_groups > 1 :
        if not edges :
            print(-1)
            return
        from_v, end_pos, cost = edges.pop()
        to_v = grid[end_pos[0]][end_pos[1]]
        if find(from_v) == find(to_v) :
            continue
        union(from_v, to_v)
        tot_cost += cost
        num_of_groups -= 1
    print(tot_cost)
solve()