import sys
from collections import deque

def solve() :
    grid = []
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(n) :
        grid.append(list(map(int, sys.stdin.readline().split())))
    max_safe_area = 0
    
    def bfs(p, q, k) :
        visited = set()
        steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
        if p != -1 : visited.add((p//m, p%m))
        if q != -1 : visited.add((q//m, q%m))
        if k != -1 : visited.add((k//m, k%m))
        safety_area = 0
        
        for i in range(n) :
            for j in range(m) :
                if (i,j) not in visited and grid[i][j] == 2 :
                    queue = deque()
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue :
                        curr_row, curr_col = queue.popleft()
                        for s in steps :
                            next_row, next_col = curr_row + s[0], curr_col+s[1]
                            if next_row >= 0 and next_row < n :
                                if next_col >= 0 and next_col < m :
                                    if (next_row, next_col) not in visited and grid[next_row][next_col] != 1:
                                        queue.append((next_row, next_col))
                                        visited.add((next_row, next_col))
        for i in range(n) :
            for j in range(m) :
                if (grid[i][j] != 1) :
                    if (i, j) not in visited :
                        safety_area += 1
        return safety_area
    
    for p in range(n * m) :
        if grid[p//m][p%m] == 0 :
            for q in range(p + 1, n * m) :
                if grid[q//m][q%m] == 0 :
                    for k in range(q + 1, n * m) :
                        if grid[k//m][k%m] == 0 :
                            max_safe_area = max(max_safe_area, bfs(p,q,k))
    
    print(max_safe_area)

solve()