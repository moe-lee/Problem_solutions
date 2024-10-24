import sys
import heapq
from collections import deque

def getEdges(key, keys, grid, edges, visited_node) :
    cv_num = keys[key]
    visited_node[cv_num] = True
    queue = deque()
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
    queue.append((*key, 0))
    visited[key[0]][key[1]] = True
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while queue :
        cr, cc, cd = queue.popleft()
        for sr, sc in steps :
            nr, nc, nd = cr + sr, cc + sc, cd + 1
            if(0<=nr<len(grid) and 0<=nc<len(grid)) :
                if not visited[nr][nc] and grid[nr][nc] != '1':
                    visited[nr][nc] = True
                    queue.append((nr, nc, nd))
                    if (nr, nc) in keys and not visited_node[keys[(nr, nc)]]:
                        heapq.heappush(edges, (nd, cv_num, keys[(nr,nc)], (nr, nc)))

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    keys = {}
    start = None
    num_of_obj = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] in ('K', 'S'):
                keys[(i,j)] = num_of_obj
                num_of_obj += 1
                if grid[i][j] == 'S' :
                    start = (i, j)
    # 이미 입력된 간선 정보는 사용하지 않는다. (무방향 그래프)
    dist = 0
    visited = [False] * (M+1)
    visited[keys[start]] = True
    edges = []
    getEdges(start, keys, grid, edges, visited)
    while not all(visited) and edges :
        cost, fromv, tov, pos = heapq.heappop(edges)
        if visited[tov] : continue
        dist += cost
        getEdges(pos, keys, grid, edges, visited)
    print(dist if all(visited) else -1)
solve()