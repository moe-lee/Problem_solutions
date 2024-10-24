import sys
import heapq

def solve() :
    n, m = map(int, sys.stdin.readline().split())
    graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m) :
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u][v] = c
        graph[v][u] = c
    
    def dijkstra(start, rtbl) :
        pq = [(0, 0, start, start)]
        included = set()
        while pq :
            cc, node_cnt, cv, pv = heapq.heappop(pq)
            if cv not in included :
                included.add(cv)
                if cv == start or pv == start :
                    pv = cv
                rtbl[cv] = pv
                if len(included) == n : return
                for nv in range(1, n+1) :
                    if graph[cv][nv] == -1 : continue
                    heapq.heappush(pq, (cc + graph[cv][nv], node_cnt + 1, nv, pv))
    # Heap에 의해 입출력하는 시간이 절대적으로 큰 시간을 할애하는 건가?
    for i in range(1, n+1) :
        route_tbl = [None] * (n+1)
        dijkstra(i, route_tbl)
        for j in range(1, n+1) :
            print(route_tbl[j] if j != i else '-', end=" ")
        print()

import sys
def solve2() :
    n, m = map(int, sys.stdin.readline().split())
    DP = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for _ in range(m) :
        u, v, c = map(int, sys.stdin.readline().split())
        DP[u][v] = c
        DP[v][u] = c
        visited[u][v] = v
        visited[v][u] = u
    
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if DP[i][j] > DP[i][k] + DP[k][j]:
                    DP[i][j] = DP[i][k] + DP[k][j]
                    visited[i][j] = visited[i][k]
    
    for i in range(1,n+1):
        for j in range(1, n+1) :
            print((visited[i][j] if j != i else "-"), end=" ")
        print()

    
solve2()