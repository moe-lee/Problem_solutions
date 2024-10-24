from collections import deque
for test_case in range(1,11) :
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    reds = deque()
    dr_cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 :
                reds.append((i,j))
    while reds :
        cr, cc = reds.popleft()
        grid[cr][cc] = 0
        nr = cr + 1
        while nr < N :
            if grid[nr][cc] in (1, 2) :
                break
            nr += 1
        if nr < N and grid[nr][cc] == 2 :
            grid[nr-1][cc] = 1
            dr_cnt += 1
    print('#' + str(test_case), dr_cnt)