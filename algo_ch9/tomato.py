import sys
from collections import deque

def solve() :
    cols, rows, tables = map(int, sys.stdin.readline().split())
    step = ((1, 0, 0),(-1, 0, 0),(0, -1, 0),(0, 1, 0),(0, 0, -1),(0, 0, 1))
    storage = []
    ripe_source = deque()
    for i in range(tables) :
        storage.append([])
        for j in range(rows) :
            storage[i].append(list(map(int, sys.stdin.readline().split())))
            for k in range(cols) :
                if storage[i][j][k] == 1 :
                    ripe_source.append((i,j,k))
    days = 0
    visited = set()
    def bfs(table, row, col) :
        visited.add((table, row, col))
        newly_riped = deque()
        cur_tab, cur_row, cur_col = table, row, col
        for s in step :
            next_tab, next_row, next_col = cur_tab + s[0], cur_row + s[1], cur_col + s[2]
            if (0<=next_tab and 0<=next_row and 0<=next_col) and (next_tab < tables and next_row < rows and next_col < cols) and (next_tab, next_row, next_col) not in visited :
                visited.add((next_tab, next_row, next_col))
                if storage[next_tab][next_row][next_col] == 0 :
                    storage[next_tab][next_row][next_col] = 1
                    newly_riped.append((next_tab, next_row, next_col))                        
        return newly_riped
    
    while ripe_source :
        second_queue = deque()
        for i, j, z in ripe_source :
            second_queue.extend(bfs(i, j, z))
        if len(second_queue) > 0 :
            days +=1
        ripe_source = second_queue
    
    for i in range(tables) :
        for j in range(rows) :
            if 0 in storage[i][j] :
                print(-1)
                return
    print(days)

solve()