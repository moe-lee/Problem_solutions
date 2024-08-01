import sys
from collections import deque

def solve() :
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 1, 0)) # row, col, dist, walls
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while queue :
        cr, cc, cd, cw = queue.popleft()
        if(cr == n-1) and (cc == m-1) :
            print(cd)
            return
        for sr, sc in steps :
            nr, nc = cr+sr, cc+sc
            if 0<=nr<n and 0<=nc<m :
                if grid[nr][nc] == 1 and cw < 1 and not visited[nr][nc][cw+1]:
                    queue.append((nr, nc, cd+1, cw+1))
                    visited[nr][nc][cw+1] = True
                elif grid[nr][nc] == 0 and not visited[nr][nc][cw] :
                    queue.append((nr, nc, cd+1, cw))
                    visited[nr][nc][cw] = True
    print(-1)
    return
solve()

'''
2 7
0100011
0001010
'''