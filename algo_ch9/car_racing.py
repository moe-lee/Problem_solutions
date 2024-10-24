import sys
from collections import defaultdict
from collections import deque
def solve() :
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = defaultdict(list)
    indegree = [0] * (N+1)
    for _ in range(M):
        p, q, r = map(int, sys.stdin.readline().split())
        graph[p].append((q, r))
        indegree[q] += 1
    max_point = [0] * (N+1)
    paths = [None for _ in range(N+1)]
    queue = deque()
    queue.append(1)
    paths[1] = [1]
    while queue :
        at = queue.popleft()
        for to, point in graph[at] :
            if max_point[to] < max_point[at] + point :
                max_point[to] = max_point[at] + point
                paths[to] = paths[at][:]
                paths[to].append(to)
            indegree[to] -= 1
            if(indegree[to] == 0 and to != 1) :
                queue.append(to)
    print(max_point[1])
    print(*paths[1])
solve()