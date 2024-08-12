import sys
from collections import defaultdict
import heapq

def solve() :
    graph = defaultdict(list)
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    for _ in range(M) :
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u].append((c, v))
    
    pre_vertex = [None] * (N+1)
    start, finish = map(int ,sys.stdin.readline().split())
    costs = {}
    def dijkstra() :
        pq = [(0, start, None)]
        while pq :
            cc, cv, pv = heapq.heappop(pq)
            if cv not in costs:
                costs[cv] = cc
                pre_vertex[cv] = pv
                for tc, nv in graph[cv] :
                    heapq.heappush(pq, (cc + tc, nv, cv))
    dijkstra()
    print(costs[finish])
    cv = finish
    stack = []
    while cv != None :
        stack.append(cv)
        cv = pre_vertex[cv]
    print(len(stack))
    while stack : print(stack.pop(), end=" ")
solve()