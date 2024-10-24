from collections import deque

for _ in range(1, 11) :
    t_num = input()
    grid = [list(map(int, list(input()))) for _ in range(16)]
    queue = deque()
    visited = [[False for _ in range(16)] for _ in range(16)]
    for i in range(16) :
        for j in range(16) :
            if grid[i][j] == 2 :
                queue.append((i,j))
                visited[i][j] = True
                break
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while queue :
        cr, cc = queue.popleft()
        if grid[cr][cc] == 3 : 
            break
        for sr, sc in steps :
            nr, nc = cr + sr, cc + sc
            if (0<=nr<16) and (0<=nc<16) and not visited[nr][nc] and grid[nr][nc] != 1:
                queue.append((nr,nc))
                visited[nr][nc] = True
    else :
        print('#'+t_num, 1)
        continue
    print('#'+t_num, 0)