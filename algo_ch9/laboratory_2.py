import sys
from collections import deque

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    viruses = []
    grid = []
    for _ in range(N) :
        grid.append(list(map(int, sys.stdin.readline().split())))
        for i in range(N) :
            if grid[-1][i] == 2 : viruses.append((len(grid) - 1, i))
    UNVISITED = float('inf')
    distmap = [[[UNVISITED for _ in range(N)] for _ in range(N)] for _ in range(len(viruses))]
    
    def BFS(row, col, idx) :
        queue = deque()
        queue.append((row, col, 0))
        distmap[idx][row][col] = 0
        steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while queue :
            cr, cc, cd = queue.popleft()
            for sr, sc in steps :
                nr, nc, nd = cr+sr, cc+sc, cd+1
                if(0<=nr<N and 0<=nc<N and grid[nr][nc] != 1) :
                    if distmap[idx][nr][nc] == UNVISITED :
                        distmap[idx][nr][nc] = nd
                        queue.append((nr, nc, nd))
    for i in range(len(viruses)) :
        BFS(viruses[i][0], viruses[i][1], i)
    
    def backtrack(virus_list, idx) :
        if len(virus_list) < M :
            total_min = float('inf')
            for i in range(idx, len(viruses)) :
                virus_list.append(i)
                total_min = min(total_min, backtrack(virus_list, i + 1))
                virus_list.pop()
            return total_min
        else :
            total_max = 0
            for i in range(N) :
                for j in range(N) :
                    if grid[i][j] == 1 : continue
                    partial_min = min([distmap[k][i][j] for k in virus_list])
                    total_max = max(total_max, partial_min)
            return total_max
    res = backtrack(virus_list=[], idx=0)
    print(res if res != float('inf') else -1)
solve()

'''
3 1
0 0 0
2 1 1
0 0 0

'''