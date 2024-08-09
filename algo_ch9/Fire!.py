import sys
from collections import deque

def solve() :
    R, C = map(int, sys.stdin.readline().split())
    grid = []
    fire = deque()
    joe = deque()
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for j in range(R) :
        line = sys.stdin.readline().strip()
        for i in range(len(line)) :
            if line[i] == 'F' :
                fire.append((j, i))
            elif line[i] == 'J' :
                joe.append((j, i, 1))
        grid.append(list(line))
    
    while joe :
        n_fire = deque()
        while fire :
            fr, fc = fire.popleft()
            for sr, sc in steps :
                nr, nc = fr+sr, fc+sc
                if 0<=nr<R and 0<=nc<C and (grid[nr][nc] == '.' or grid[nr][nc] == 'J') :
                    n_fire.append((nr, nc))
                    grid[nr][nc] = 'F'
        n_joe = deque()
        while joe :
            jr, jc, cd = joe.popleft()
            if (jr == R-1) or (jc == C-1) or (jr == 0) or (jc == 0) :
                print(cd)
                return
            for sr, sc in steps :
                nr, nc = jr+sr, jc+sc
                if 0<=nr<R and 0<=nc<C and grid[nr][nc] == '.' :
                    if (nr == R-1) or (nc == C-1) or (nr == 0) or (nc == 0) :
                        print(cd +1)
                        return
                    n_joe.append((nr, nc, cd + 1))
                    grid[nr][nc] = 'J'
        fire = n_fire
        joe = n_joe
    print('IMPOSSIBLE')
    return
solve()