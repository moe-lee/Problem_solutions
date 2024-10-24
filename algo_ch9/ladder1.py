def travel(grid, col) :
    cr, cc = 0, col
    side = (-1, 1)
    dist = 0
    while cr < 100 :
        for dx in side :
            nc = cc + dx
            if 0<=nc<100 and grid[cr][nc] == 1:
                while 0 <= cc + dx < 100 and grid[cr][cc + dx] != 0 :
                    dist += 1
                    cc += dx
                break
        cr += 1
        dist += 1
    return dist

for _ in range(10) :
    t_num = input()
    grid = [list(map(int, input().split())) for _ in range(100)]
    dists = [[] for _ in range(100*100 + 1)]
    for i in range(100) :
        if grid[0][i] == 1 :
            dist = travel(grid, i)
            dists[dist].append(i)
    for i in range(0, 100*100 + 1) :
        if dists[i] :
            print('#'+t_num, *dists[i])
            break