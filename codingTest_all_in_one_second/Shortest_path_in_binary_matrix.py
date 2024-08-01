from collections import deque

def getShortestPath(grid) :
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    if grid[0][0] == 1 : return -1
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True 
    offset = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    while queue :
        cur_row, cur_col, cur_distance = queue.popleft()
        if cur_row == n-1 and cur_col == n-1 :
            return cur_distance
        for o in offset :
            next_row, next_col = cur_row + o[0], cur_col + o[1]
            if next_row >= 0 and next_row < n and next_col >= 0 and next_col < n :
                if not visited[next_row][next_col] and grid[next_row][next_col] == 0:
                    queue.append((next_row, next_col, cur_distance + 1))
                    visited[next_row][next_col] = True
    return -1

grid = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
print(getShortestPath(grid))