import sys
from collections import defaultdict
from collections import deque
def solve():
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    indegree = [0] * (N+1)
    ordering = []
    for _ in range(M) :
        line = list(map(int, sys.stdin.readline().split()))
        for i in range(2, len(line)) :
            graph[line[i-1]].append(line[i])
            indegree[line[i]] += 1
    
    queue = deque()
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            queue.append(i)
            ordering.append(i)
    
    while queue :
        cv = queue.popleft()
        for nv in graph[cv] :
            indegree[nv] -= 1
            if indegree[nv] == 0 :
                ordering.append(nv)
                queue.append(nv)
    if len(ordering) != N : print(0)
    else:
        for i in ordering : print(i)
solve()