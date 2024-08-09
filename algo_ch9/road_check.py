import sys
from collections import defaultdict
import heapq

def solve() :
    N, M = map(int ,sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M) :
        a, b, t = map(int ,sys.stdin.readline().split())
        graph[a].append((t, b))
        graph[b].append((t, a))
    # 1 to N
    def dijkstra(blocked) :
        precedings = [None] * (N + 1)
        pq = [(0, 1, None)] # cost, vertex
        costs = [float('inf') for _ in range(N + 1)]
        while pq :
            cc, cv, pv = heapq.heappop(pq)
            if costs[cv] == float('inf') :
                if pv is not None :
                    precedings[cv] = pv
                costs[cv] = cc
                for cost, nv in graph[cv] :
                    if nv not in blocked or cv not in blocked :
                        heapq.heappush(pq, (cost + cc, nv, cv))
        return (precedings, costs)
    precedings, costs = dijkstra([])
    minimum_cost = costs[N]
    max_delay = 0
    u, v = precedings[N], N
    while u is not None :
        _, costs = dijkstra((u, v))
        max_delay = max(max_delay, costs[N] - minimum_cost)
        u, v = precedings[u], u
    print(max_delay if max_delay != float('inf') else -1)
    return
solve()