import sys
import heapq
from collections import defaultdict
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M) :
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u].append((c, v))
        graph[v].append((c, u))
    
    next_vertex = [[] for _ in range(N+1)]
    costs = {}
    cnt = 0
    pq = [(0, 1, None)]
    while pq :
        cc, cv, pv = heapq.heappop(pq)
        if cv not in costs :
            if pv is not None :
                cnt+=1
                next_vertex[pv].append(cv)
            costs[cv] = cc
            for tc, nv in graph[cv] :
                nc = tc + cc
                heapq.heappush(pq, (nc, nv, cv))
    print(cnt)
    for i in range(1, N+1) :
        for nv in next_vertex[i] :
            print(i, nv)
solve()