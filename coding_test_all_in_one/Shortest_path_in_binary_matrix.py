from collections import deque

import heapq

def BFS(graph, start_v) :
    queue = deque(start_v)
    visited = [start_v]
    while queue :
        cur_v = queue.popleft()
        for v in graph[cur_v] :
            if v not in visited :
                visited.append(v)
                queue.append(v)
    return visited

def shortestPathBinaryMatrix(graph) :
    n = len(graph)
    dcol = [-1, 0, 1, -1, 1, -1, 0, 1]
    drow = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    queue = deque()
    if(graph[0][0] == 1) or graph[-1][-1] == 1:
        print(-1)
        return
    
    queue.append((0, 0, 1))
    visited = [[False] * n for _ in range(n)]
    
    visited[0][0] = True
    
    while queue :
        cur_row, cur_col, cur_step = queue.popleft()
        
        if cur_row == n-1 and cur_col == n-1 :
            print(cur_step)
            return
        
        for i in range(8) :
            next_row = cur_row + drow[i]
            next_col = cur_col + dcol[i]
            if(0 <= next_row and next_row < n and 0 <= next_col and next_col < n):
                if (graph[next_row][next_col] == 0 and not visited[next_row][next_col]) :
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col, cur_step + 1))
    print(-1)
    return

grid = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0]
]

shortestPathBinaryMatrix(grid)


def BFS(graph, start) :
    queue = deque()
    visited = [False] * len(graph)
    queue.append(start)
    visited[start] = True
    
    while queue :
        cur_v = queue.popleft()
        for nv in graph[cur_v] :
            if not visited[nv] :
                visited[nv] = True
                queue.append(nv)

def DFS(graph, visited, cur_v) :
    for nv in graph[cur_v] :
        if nv not in visited :
            visited.append(nv)
            visited = DFS(graph, visited=visited, cur_v=nv)
    return visited

def dijkstra(graph, start, final, n) :
    pq = []
    costs = {}
    heapq.heappush(pq, (0, start))
    while pq :
        cc, cv = heapq.heappop(pq)
        if cv not in costs :
            costs[cv] = cc
            for cost, nv in graph[cv] :
                nc = cost + cc
                heapq.heappush(pq, (nc, nv))
    return costs[final]

def bellemFord(edges, start, final, n) :
    costs = [float('inf')] * n
    for _ in range(n) :
        for u, v, w in edges :
            if costs[v] > costs[u] + w :
                costs[v] = costs[u] + w
    
    for u, v, w in edges :
        if costs[v] > costs[u] + w :
            raise Exception('음수 사이클')
    return costs[final]


def floydWashallEx(edges, n) :
    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for u, v, w in edges :
        dist[u][v] = w
    
    for k in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(dist)