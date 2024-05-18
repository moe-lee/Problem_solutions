from collections import deque
def bfs(graph, start_v) :
    queue = deque(start_v)
    visited = [start_v]
    while queue:
        cur_node = queue.popleft()
        for v in graph[cur_node] :
            if v not in visited :
                visited.append(v)
                queue.append(v)
    return visited

graph = []
visited = []

def dfs(cur_v) :
    visited.append(cur_v)
    for v in graph[cur_v] :
        if v not in visited:
            dfs(v)
