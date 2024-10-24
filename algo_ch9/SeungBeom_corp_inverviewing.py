import sys
import heapq
from collections import defaultdict
def solve() :
    N, M, K = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    min_cost = [float('inf') for _ in range(N + 1)]
    min_cost[0] = 0
    for _ in range(M) :
        u, v, c = map(int, sys.stdin.readline().split())
        graph[v].append((c, u))
    dest = set()
    for v in map(int, sys.stdin.readline().split()) :
        dest.add(v)
    
    def dijkstra() :
        pq = [(0, start) for start in dest]
        visited = [False] * (N+1)
        while pq :
            cc, cv = heapq.heappop(pq)
            if not visited[cv] :
                min_cost[cv] = cc
                visited[cv] = True
                for nc, nv in graph[cv] :
                    if nv not in dest and not visited[nv] :
                        heapq.heappush(pq, (cc + nc, nv))
    dijkstra()
    tot_max = 0
    for i in range(1, N+1) :
        if min_cost[i] != float('inf') and min_cost[tot_max] < min_cost[i]: tot_max = i
    print(tot_max)
    print(min_cost[tot_max])
solve()