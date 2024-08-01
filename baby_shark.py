import sys
from collections import deque

def solve() :
    N = int(sys.stdin.readline())
    grid = []
    for _ in range(N) :
        grid.append(list(map(int, sys.stdin.readline().split())))
        if 9 in grid[-1] :
            shark_row = len(grid) - 1
            shark_col = grid[-1].index(9)
    
    steps = (((-1, 0), None), ((0, -1), (0, 1)), ((1, 0), None))
    shark_before = (-1, -1)
    shark_size = 2
    eaten_fishes = 0
    passed_time = 0
    
    def BFS(row, col) :
        first_queue = deque()
        second_queue = deque()
        first_queue.append((row, col, 0))
        visited = set()
        visited.add((row, col))
        while first_queue :
            for s in steps:
                for c in first_queue :
                    for sb in s :
                        if sb is None : continue
                        next_row = c[0] + sb[0]
                        next_col = c[1] + sb[1]
                        if 0 <= next_row and next_row < N and 0 <= next_col and next_col < N :
                            if (next_row, next_col) not in visited :
                                visited.add((next_row, next_col))
                                if grid[next_row][next_col] == 0 or grid[next_row][next_col] == shark_size :
                                    second_queue.append((next_row, next_col, c[2] + 1))
                                elif grid[next_row][next_col] < shark_size :
                                    return (next_row, next_col, c[2] + 1)
            first_queue = second_queue
            second_queue = deque()
        return (row, col, 0)
    
    while shark_before != (shark_row, shark_col) :
        shark_before = (shark_row, shark_col)
        (shark_row, shark_col, sec) = BFS(row=shark_row, col=shark_col)
        passed_time += sec
        grid[shark_before[0]][shark_before[1]] = 0
        grid[shark_row][shark_col] = 9
        if shark_before != (shark_row, shark_col) :
            eaten_fishes += 1
        if eaten_fishes % shark_size == 0 :
            eaten_fishes = 0
            shark_size += 1
    print(passed_time)
    
solve()