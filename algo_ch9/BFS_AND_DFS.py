import sys
from collections import deque
from collections import defaultdict
def solve() :
    N, M, S = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M) :
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (N+1)
    def DFS(cv) :
        visited[cv] = True
        print(cv, end=" ")
        graph[cv].sort()
        for nv in graph[cv] :
            if not visited[nv] : DFS(nv)
        return
    def BFS() :
        queue = deque()
        visited = [False] * (N+1)
        queue.append(S)
        visited[S] = True
        while queue :
            cv = queue.popleft()
            print(cv, end=" ")
            graph[cv].sort()
            for nv in graph[cv] :
                if not visited[nv] :
                    visited[nv] = True
                    queue.append(nv)
    
    DFS(S)
    print()
    BFS()
solve()