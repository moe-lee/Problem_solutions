from collections import deque
from collections import defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m) :
    u, v, limit = map(int, input().split())
    graph[u].append((v, limit))
    graph[v].append((u, limit))
start, finish = map(int, input().split())

def BFS(limit) :
    queue = deque()
    visited = [False] * (n+1)
    queue.append(start)
    visited[start] = True
    while queue :
        cv = queue.popleft()
        if cv == finish : return True
        for v, w in graph[cv] :
            if w >= limit and not visited[v]:
                visited[v] = True
                queue.append(v)
    return False

left, right = 1, 10**9 + 1
while left < right :
    limit = (left + right) // 2
    reachable = BFS(limit=limit)
    if not reachable :
        right = limit
    else :
        left = limit + 1
print(left - 1)

'''
4 3
1 2 1000000000
2 3 1000000000
3 4 1000000000
1 4



'''