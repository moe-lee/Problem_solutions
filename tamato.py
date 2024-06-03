import sys
from collections import deque

def solve() :
    grid = []
    m,n = map(int, sys.stdin.readline().split())
    visited = set()
    queue_first = deque()
    for i in range(n) :
        grid.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m) :
            if grid[i][j] == 1:
                queue_first.append((i, j))
                visited.add((i, j))
    
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    days = 0
    while queue_first :
        queue_second = deque()
        changed = False
        while queue_first :
            curr_row, curr_col = queue_first.popleft()
            for s in steps:
                next_row, next_col = curr_row + s[0], curr_col + s[1]
                if next_row >= 0 and next_row < n and next_col >= 0 and next_col < m :
                    if grid[next_row][next_col] == 0 :
                        grid[next_row][next_col] = 1
                        queue_second.append((next_row, next_col))
                        if not changed : 
                            days += 1
                            changed = True
        queue_first = queue_second
    
    for i in range(n) :
        for j in range(m) :
            if grid[i][j] == 0:
                print(-1)
                return
    print(days)
    return

solve()