import sys
from collections import defaultdict
from collections import deque
def solve() :
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    indegree = [0] * (N+1)
    ordering = []
    for _ in range(M) :
        u, v = map(int, sys.stdin.readline().split())
        indegree[v] += 1
        graph[u].append(v)
    q = deque()
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            q.append(i)
            ordering.append(i)
    while q :
        cv = q.popleft()
        for nv in graph[cv] :
            indegree[nv] -= 1
            if indegree[nv] == 0 :
                q.append(nv)
                ordering.append(nv)
    print(*ordering)
solve()