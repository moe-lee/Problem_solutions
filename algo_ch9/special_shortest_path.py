import heapq
import sys
from collections import defaultdict
def solve() :
    N, E = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(E) :
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    v1, v2 = map(int, sys.stdin.readline().split())
    cost_v1 = dict()
    cost_v2 = dict()
    
    def dijkstra(start, costs) :
        pq = []
        pq.append((0, start))
        while pq :
            cur_cost, cur_vertex = heapq.heappop(pq)
            if cur_vertex not in costs :
                costs[cur_vertex] = cur_cost
                for cost, next_vertex in graph[cur_vertex] :
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_vertex))
    dijkstra(v1, cost_v1)
    dijkstra(v2, cost_v2)
    if v2 not in cost_v1 or 1 not in cost_v1 or N not in cost_v1:
        return -1
    return min(cost_v1[1] + cost_v1[v2] + cost_v2[N], cost_v2[1] + cost_v1[v2] + cost_v1[N])

print(solve())