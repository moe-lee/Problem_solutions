import sys
from collections import deque

def solve2() :
    N, M = map(int, sys.stdin.readline().split())
    grid = []
    virus = []
    for i in range(N) :
        grid.append(list(map(int,sys.stdin.readline().split())))
        for j in range(N) :
            if grid[-1][j] == 2 :
                virus.append((i, j))
    steps = ((-1,0),(1,0),(0,-1),(0,1))
    boards = [[[float('inf') for _ in range(N)] for _ in range(N)] for _ in range(len(virus))]
    
    def BFS(row, col, board) :
        visited = set()
        queue = deque()
        queue.append((row, col, 0))
        visited.add((row, col))
        board[row][col] = 0
        while queue :
            cr, cc, cd = queue.popleft()
            for sr, sc in steps :
                nr, nc, nd = cr+sr, cc+sc, cd + 1
                if (0<=nr<N)and(0<=nc<N)and(grid[nr][nc] != 1) :
                    if (nr, nc) not in visited :
                        board[nr][nc] = nd
                        visited.add((nr, nc))
                        queue.append((nr, nc, nd))
    
    for i in range(len(virus)) :
        BFS(virus[i][0], virus[i][1], boards[i])
    
    def getMaxDist(viruses, cur_i) :
        if(len(viruses) < M) :
            min_val = float('inf')
            for i in range(cur_i + 1, len(virus) - (M - 1 - len(viruses))) :
                viruses.append(i)
                min_val = min(min_val, getMaxDist(viruses, i))
                viruses.pop()
            return min_val
        else :
            max_dist = 0
            for i in range(N) :
                for j in range(N) :
                    if grid[i][j] in (2, 1) :
                        continue
                    else :
                        tmp_min = float('inf')
                        unreachables = 0
                        for vi in viruses :
                            if boards[vi][i][j] == float('inf') :
                                unreachables += 1
                            tmp_min = min(tmp_min, boards[vi][i][j])
                        if unreachables == len(viruses) : return float('inf')
                        max_dist = max(max_dist, tmp_min)
            return max_dist
    ans = getMaxDist([], -1)
    print(ans if ans != float('inf') else -1)
solve2()