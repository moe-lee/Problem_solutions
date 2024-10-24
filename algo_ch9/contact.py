from collections import defaultdict

for test_case in range(1, 11) :
    N, start = map(int, input().split())
    graph = defaultdict(list)
    edges = list(map(int, input().split()))
    visited = [False] * (101)
    for i in range(N // 2) :
        graph[edges[i*2]].append(edges[i*2+1])
    next_nodes = [start]
    last_visited = None
    while next_nodes :
        last_visited = next_nodes[:]
        candidates = []
        for node in next_nodes :
            for nv in graph[node] :
                if not visited[nv] :
                    visited[nv] = True
                    candidates.append(nv)
        next_nodes = candidates
    print('#'+str(test_case), max(last_visited))