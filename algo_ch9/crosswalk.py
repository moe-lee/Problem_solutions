import sys
import heapq
UNVISITED = float('inf')

def solve() :
    N,M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M) :
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append((v, i))
        graph[v].append((u, i))
    visit_time = [UNVISITED] * (N+1)
    # total wait time, current node number
    pq = [(0, 1)] 
    # current time in cycle = (total wait time) % M
    while pq :
        tot_vtime, cur_node = heapq.heappop(pq)
        if cur_node == N :
            print(tot_vtime + 1)
            return
        if visit_time[cur_node] == UNVISITED :
            visit_time[cur_node] = tot_vtime
            for nv, mi in graph[cur_node] :
                if(visit_time[nv] != UNVISITED) : continue
                heapq.heappush(pq, (tot_vtime + ((mi - (tot_vtime%M)) + M) % M, nv))
    print(-1)
    return
solve()