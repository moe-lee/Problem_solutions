from collections import deque

def numIslands(grid) :
    number_of_islands = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def bfs(x, y) :
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        while queue :
            cur_x, cur_y = queue.popleft()
            for i in range(4) :
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n :
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y] :
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
            
    
    for i in range(rows) :
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j] :
                number_of_islands += 1
                bfs(i, j)
    
    return number_of_islands

grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]

numIslands(grid=grid)