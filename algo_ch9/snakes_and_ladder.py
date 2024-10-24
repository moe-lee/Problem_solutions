import sys
import heapq
def solve() :
    N, M = map(int,sys.stdin.readline().split())
    snakes_ladders = dict()
    for _ in range(N+M) :
        u, v = map(int, sys.stdin.readline().split())
        snakes_ladders[u] = v
    
    min_cost = [float('inf') for _ in range(101)]
    pq = [(0, 1)]
    
    while pq :
        cm, cv = heapq.heappop(pq)
        if min_cost[cv] == float('inf') :
            min_cost[cv] = cm
            if cv == 100 : break
            for i in range(1, 7) :
                if i + cv <= 100 :
                    if i + cv in snakes_ladders :
                        heapq.heappush(pq, (cm + 1, snakes_ladders[cv + i]))
                    else :
                        heapq.heappush(pq, (cm + 1, cv + i))
    
    print(min_cost[100])
solve()