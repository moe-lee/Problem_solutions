from collections import defaultdict
from collections import deque
for _ in range(1, 11) :
    t_num, M = map(int, input().split())
    graph = defaultdict(list)
    edges = list(map(int, input().split()))
    for i in range(M) :
        graph[edges[i*2]].append(edges[i*2+1])
    queue = deque()
    queue.append(0)
    visited = [False] * (100)
    res = 0
    print('#'+str(t_num), end=" ")
    while queue :
        cv = queue.popleft()
        if cv == 99 :
            break
        for nv in graph[cv] :
            if not visited[nv] :
                queue.append(nv)
                visited[nv] = True
    else :
        print(0)
        continue
    print(1)