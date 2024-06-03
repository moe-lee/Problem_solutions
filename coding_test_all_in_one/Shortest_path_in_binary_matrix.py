from collections import deque
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