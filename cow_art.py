import sys
from collections import deque
def solve() :
    N = int(sys.stdin.readline())
    grid = []
    for i in range(N) :
        grid.append(list(sys.stdin.readline().strip()))
        
    
    regions = { 'human' : 0, 'cow' : 0 }
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = set()
    
    def BFS(row, col) :
        queue = deque()
        queue.append((row, col))
        second_queue = deque()
        visited.add((row, col))
        while queue :
            curr_row, curr_col = queue.popleft()
            for s in steps :
                next_row, next_col = curr_row + s[0], curr_col + s[1]
                if 0 <= next_row and next_row < N and 0 <= next_col and next_col < N and (next_row, next_col) not in visited :
                    if grid[curr_row][curr_col] == grid[next_row][next_col] :
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
                    elif grid[curr_row][curr_col] != 'B' and grid[next_row][next_col] != 'B' :
                        second_queue.append((next_row, next_col))
            if not queue :
                regions['human'] += 1
                if second_queue :
                    next_row, next_col = second_queue.popleft()
                    while second_queue and (next_row, next_col) in visited :
                        next_row, next_col = second_queue.popleft()
                    if (next_row, next_col) not in visited :
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
        
        regions['cow'] += 1
    
    for i in range(N) :
        for j in range(N) :
            if (i, j) not in visited :
                BFS(i, j)
    print(regions['human'], regions['cow'])

solve()