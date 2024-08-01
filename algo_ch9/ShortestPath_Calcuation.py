import heapq
import sys
def solve() :
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    costs = {}
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))
    start, final = map(int, sys.stdin.readline().split())
    pq = [(0, start)]
    
    while pq :
        cur_cost, cur_vertex = heapq.heappop(pq)
        if cur_vertex not in costs :
            costs[cur_vertex] = cur_cost
            for cost, next_vertex in graph[cur_vertex] :
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_vertex))
    print(costs[final])

solve()
