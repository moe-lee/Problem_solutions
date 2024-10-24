import sys
import heapq
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u].append((c, v))
        graph[v].append((c, u))
    pq = [(0, 1)]
    cost_fox = {}
    while pq :
        if len(cost_fox) == N: break
        cc, cv = heapq.heappop(pq)
        if cv not in cost_fox :
            cost_fox[cv] = cc
            for ac, nv in graph[cv] :
                if nv not in cost_fox :
                    heapq.heappush(pq, (cc + ac, nv))
    
    cost_wolf = [0, {}, 0, 0, {}]
    pq = [(0, 1, 4)]
    while pq :
        if len(cost_wolf[1]) == len(cost_wolf[4]) and len(cost_wolf[1]) == N : break
        cc, cv, cs = heapq.heappop(pq)
        if cv not in cost_wolf[cs] :
            cost_wolf[cs][cv] = cc
            for ac, nv in graph[cv] :
                nc = cc + ac / (cs / 2)
                ns = 1 if cs == 4 else 4
                if nv not in cost_wolf[ns] :
                    heapq.heappush(pq, (nc, nv, ns))
    fox_first = 0
    for i in range(2, N+1) :
        if i in cost_fox :
            if cost_fox[i] < min(cost_wolf[1].get(i, float('inf')), cost_wolf[4].get(i, float('inf'))) :
                fox_first += 1
    print(fox_first)
solve()