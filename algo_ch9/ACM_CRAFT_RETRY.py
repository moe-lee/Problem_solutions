import sys
from collections import defaultdict
from collections import deque
def solve() :
    N, K = map(int, sys.stdin.readline().split())
    costs = list(map(int, sys.stdin.readline().split()))
    max_cost_so_far = [0] * (N+1)
    graph = defaultdict(list)
    indegree = [0] * (N+1)
    
    for _ in range(K) :
        u, v = map(int, sys.stdin.readline().split())
        indegree[v] += 1
        graph[u].append(v)
    target = int(sys.stdin.readline())
    
    queue = deque()
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            queue.append((i, 0))
    
    while queue :
        cv, cc = queue.popleft()
        for nv in graph[cv] :
            max_cost_so_far[nv] = max(max_cost_so_far[nv], cc + costs[cv-1])
            indegree[nv] -= 1
            if indegree[nv] == 0 :
                queue.append((nv, max_cost_so_far[nv]))
    print(max_cost_so_far[target] + costs[target - 1])

def service() :
    T = int(sys.stdin.readline())
    while(T) :
        solve()
        T -= 1

service()

'''
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4

'''