import sys
from collections import deque
def solve() :
    K = int(sys.stdin.readline())
    w, h = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[[False]*(K+1) for _ in range(w)] for _ in range(h)]
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    jumps = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))
    queue = deque()
    queue.append((0, 0, 0, 0)) # cr, cc, cd, ck
    visited[0][0][0] = True
    while queue :
        cr, cc, cd, ck = queue.popleft()
        if (cr, cc) == (h - 1, w - 1) :
            print(cd)
            return
        if ck < K :
            for jr, jc in jumps :
                nr, nc, nd, nk = cr + jr, cc + jc, cd + 1, ck + 1
                if 0<=nr<h and 0<=nc<w and grid[nr][nc] != 1 and not visited[nr][nc][nk] :
                    visited[nr][nc][nk] = True
                    queue.append((nr,nc,nd,nk))
        for sr, sc in steps :
            nr, nc, nd, nk = cr + sr, cc + sc, cd + 1, ck
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] != 1 and not visited[nr][nc][nk] :
                visited[nr][nc][nk] = True
                queue.append((nr,nc,nd,nk))
    
    print(-1)
    return
solve()


# 반복문 사용 때문에 여전히 일방적인 연산만 발생한다.  <- 방향의 연산이 필요하다.
'''
1
7 8
0 0 0 0 0 0 0
1 1 1 1 1 1 0
1 1 1 1 1 1 0
0 0 0 1 1 1 0
0 1 1 1 0 0 0
0 1 1 1 1 1 1
0 1 1 1 1 1 1
0 0 0 0 0 0 0


3% 오답 반례 1
30
7 10
0 1 1 1 0 1 1
1 1 0 1 1 1 0
1 1 1 1 1 1 1
1 1 1 1 1 0 1
1 1 1 0 1 1 1
1 0 1 1 1 1 1
1 1 1 1 1 1 1
1 1 0 1 1 1 1
1 1 1 1 0 1 1
1 1 1 1 1 1 0


2
2 6
0 1
1 1
1 0
1 1
0 1
0 0
'''