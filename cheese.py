import sys
from collections import deque

def solve() :
    grid = []
    n, m = map(int, sys.stdin.readline().split())
    cheese_area = 0
    hours = 0
    step = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for _ in range(n) :
        grid.append(list(map(int,sys.stdin.readline().split())))
        cheese_area += sum(grid[-1])
    
    while cheese_area > 0 :
        hours += 1
        melted_area = 0
        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        while queue :
            curr_row, curr_col = queue.popleft()
            if grid[curr_row][curr_col] :
                melted_area += 1
                grid[curr_row][curr_col] = 0
                continue
            for x, y in step :
                next_row = curr_row + x
                next_col = curr_col + y
                if 0 <= next_row and next_row < n :
                    if 0<= next_col and next_col < m :
                        if (next_row, next_col) not in visited :
                            queue.append((next_row, next_col))
                            visited.add((next_row, next_col))
        if cheese_area - melted_area == 0 :
            print(hours)
            print(melted_area)
        cheese_area -= melted_area
    return

solve()