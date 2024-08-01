'''
grid = [['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']]
'''
grid = [['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']]

from collections import deque

def numberOfIslands(grid) :
    m = len(grid)
    n = len(grid[0])
    visited = [[False] * n for _ in range(m)]
    
    def bfs(i, j) :
        steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        while queue :
            cur_row, cur_col = queue.popleft()
            for s in steps :
                next_row, next_col = cur_row + s[0], cur_col + s[1]
                if next_row >= 0 and next_row < len(grid) :
                    if next_col >= 0 and next_col < len(grid[0]) :
                        if not visited[next_row][next_col] and grid[next_row][next_col] == '1' :
                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))
    
    num_of_islands = 0
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            if not visited[i][j] and grid[i][j] == '1' :
                num_of_islands += 1
                bfs(i, j)
    return num_of_islands

print(numberOfIslands(grid=grid))