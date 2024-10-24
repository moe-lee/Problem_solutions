import sys
from collections import defaultdict
from collections import deque
def solve() :
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = defaultdict(list)
    numOfParts = [[0 for _ in range(N+1)] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(M) :
        x, y, z = map(int, sys.stdin.readline().split())
        graph[y].append((x, z))
        indegree[x] += 1
    
    queue = deque()
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            queue.append(i)
            numOfParts[i][i] = 1
    
    while queue :
        cv = queue.popleft()
        for nv, cost in graph[cv] :
            for j in range(1, N+1) :
                numOfParts[nv][j] += cost * (numOfParts[cv][j])
            indegree[nv] -= 1
            if indegree[nv] == 0 :
                queue.append(nv)
    
    for i in range(1, N) :
        if numOfParts[N][i] == 0 : continue
        print(i, numOfParts[N][i])
solve()