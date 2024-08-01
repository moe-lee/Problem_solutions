import sys
import heapq
from collections import defaultdict

def solve() :
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    graph = defaultdict(list)
    for _ in range(E) :
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))
    costs = {}
    pq = []
    pq.append((0, K))
    while pq :
        cur_cost, cur_vertex = heapq.heappop(pq)
        if cur_vertex not in costs :
            costs[cur_vertex] = cur_cost
            for cost, next_vertex in graph[cur_vertex] :
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_vertex))
    
    for i in range(1, V + 1) :
        if i not in costs :
            print('INF')
        else :
            print(costs[i])

solve()