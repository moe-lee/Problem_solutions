import sys
import heapq
from collections import defaultdict

def solve() :
    n, m, x = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    longest_amount = 0
    for _ in range(m) :
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u].append((t,v))

    def dijkstra(start, is_x) :
        costs = {}
        pq = [(0, start)]
        while pq :
            cc, cv = heapq.heappop(pq)
            if cv not in costs :
                costs[cv] = cc
                for c, nv in graph[cv] :
                    nc = c + cc
                    heapq.heappush(pq, (nc, nv))
        if is_x : return costs
        else : return costs[x]
    shortest_path_to_x = dijkstra(x, True)
    for i in range(1, n+1) :
        if i != x :
            longest_amount = max(longest_amount, shortest_path_to_x[i] + dijkstra(i, False))
    print(longest_amount)

solve()