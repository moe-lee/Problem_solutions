import sys
import heapq
from collections import defaultdict
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    gas_costs = [0] + list(map(int, sys.stdin.readline().split()))
    graph = defaultdict(list)
    for _ in range(M) :
        u, v, d = map(int, sys.stdin.readline().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    minimum_cost_so_far = [float('inf') for _ in range(N+1)]
    pq = [(0, 1, 1)] # format : total_cost_so_far, minimum_GS_so_far, cur_node
    while pq :
        tot_cost_sf, min_gs_sf, cv = heapq.heappop(pq)
        if cv == N :
            print(tot_cost_sf)
            return
        if minimum_cost_so_far[cv] > gas_costs[min_gs_sf] :
            minimum_cost_so_far[cv] = gas_costs[min_gs_sf]
            for nv, dist in graph[cv] :
                next_costs = tot_cost_sf + (minimum_cost_so_far[cv] * dist)
                next_min_gs = min_gs_sf if gas_costs[min_gs_sf] < gas_costs[nv] else nv
                if minimum_cost_so_far[nv] > gas_costs[next_min_gs] :
                    heapq.heappush(pq, (next_costs, next_min_gs, nv))
solve()


'''
test #1 : 모든 비용이 1
5 5
1 1 1 1 1
1 2 1
1 3 1
2 5 1
3 4 1
4 5 1

'''