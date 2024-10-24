import sys
import heapq
from collections import defaultdict
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    pq = []
    indegree = [0] * (N+1)
    graph = defaultdict(list)
    for _ in range(M) :
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        indegree[v] += 1
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            heapq.heappush(pq, i)
    visited = []
    while pq :
        cv = heapq.heappop(pq)
        visited.append(cv)
        for next_vertex in graph[cv] :
            indegree[next_vertex] -= 1
            if indegree[next_vertex] == 0 :
                heapq.heappush(pq, next_vertex)
    print(*visited)
solve()

'''
test #1
5 5
3 2
1 2
1 3
4 1
5 1

ans : 4 5 1 3 2
'''