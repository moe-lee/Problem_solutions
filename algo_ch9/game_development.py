import sys
from collections import defaultdict
from collections import deque

def solve() :
    N = int(sys.stdin.readline())
    required_time = [0 for _ in range(N+1)]
    cost = {}
    graph = defaultdict(list)
    indegree = [0 for _ in range(N+1)]
    for i in range(1, N+1) :
        tokens = list(map(int,sys.stdin.readline().split()))
        cost[i] = tokens[0]
        for j in range(1, len(tokens) - 1) :
            graph[tokens[j]].append(i)
            indegree[i] += 1
    
    queue = deque()
    for i in range(1, N+1) :
        if indegree[i] == 0 : 
            queue.append(i)
    
    while queue :
        cv = queue.popleft()
        required_time[cv] += cost[cv]
        for nv in graph[cv] :
            indegree[nv] -= 1
            required_time[nv] = max(required_time[nv], required_time[cv])
            if indegree[nv] == 0 :
                queue.append(nv)
    for t in required_time[1:] : print(t)
solve()