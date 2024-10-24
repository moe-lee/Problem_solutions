import sys
from collections import defaultdict
from collections import deque

def solve() :
    N, M = int(sys.stdin.readline()), int(sys.stdin.readline())
    graph = defaultdict(list)
    indegree = [0 for _ in range(N+1)]
    precedes = [[] for _ in range(N+1)] # precedes는 후 BFS의 graph가 된다.
    maximum_at = [0 for _ in range(N+1)]
    for _ in range(M) :
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u].append((v,t))
        indegree[v] += 1
    S, T = map(int, sys.stdin.readline().split())
    # Top-sorting, kahn's algorithm.
    queue = deque()
    queue.append(S)
    while queue :
        cv = queue.popleft()
        for nv, cost in graph[cv] :
            if maximum_at[cv] + cost >= maximum_at[nv] :
                tmp = maximum_at[nv]
                maximum_at[nv] = maximum_at[cv] + cost
                if tmp == maximum_at[nv] :
                    precedes[nv].append(cv)
                else : precedes[nv] = [cv]
            indegree[nv] -= 1
            if indegree[nv] == 0 :
                queue.append(nv)
    queue = deque()
    queue.append(T)
    edge_cnt = 0
    visited = [False] * (N+1)
    visited[T] = True
    while queue :
        cv = queue.popleft()
        for nv in precedes[cv] :
            edge_cnt += 1
            if not visited[nv] :
                visited[nv] = True
                queue.append(nv)
    print(maximum_at[T])
    print(edge_cnt)
solve()