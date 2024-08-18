import sys
from collections import deque
import copy

## 어떤 궁수가 먼저 쏴야하는가?
### 반복문 -> 왼쪽 궁수부터 쏘게 됨. -> 동시에 쏘는 경우를 반영할 수 없음.

def BFS(grid, N, M, col, D, dead_enemies) :
    q1 = deque()
    q1.append((N, col, 0))
    step = ((0, -1), (-1, 0), (0, 1))
    visited = set()
    visited.add((N, col))
    while q1 :
        q2 = deque()
        for sr, sc in step :
            for cr, cc, cd in q1 :
                if cr < N and (grid[cr][cc] == 1 or (cr,cc) in dead_enemies) :
                    # 비록 다른 궁수가 쏜 적이라도, 동시에 쏘기 때문에 다른 궁수도 이 적이 가장 가깝다면 쏴야한다.
                    # 다른 궁수가 안 쐈다면
                    if (grid[cr][cc] == 1) :
                        grid[cr][cc] = 0
                        dead_enemies.add((cr, cc))
                        return 1
                    else : # 다른 궁수가 쐈다면
                        return 0
                if cd == D :
                    continue
                nr, nc, nd = cr+sr, cc+sc, cd + 1
                if(0<=nr<N and 0<=nc<M and ((nr, nc) not in visited)) :
                    visited.add((nr, nc))
                    q2.append((nr, nc, nd))
        q1 = q2
    return 0

def search(grid, N, M, acher, D) :
    enemy_cnt = 0
    for castle_row in range(N, 0, -1) :
        dead_enemies = set()
        for acher_col in acher :
            enemy_cnt += BFS(grid, castle_row, M, acher_col, D, dead_enemies)
    return enemy_cnt
## 완전탐색 적용 -> 최적 위치를 바로 판단하기 어려우며, DP 적용 X (Optimal substructure가 아님.)
def solve() :
    N, M, D = map(int, sys.stdin.readline().split())
    grid_o = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    ans = 0
    for i in range(0, M-2) :
        for j in range(i+1, M-1) :
            for k in range(j + 1, M) :
                ans = max(ans, search(copy.deepcopy(grid_o), N, M, (i, j, k), D))
    print(ans)
solve()


'''
15 3 1
1 0 1
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0

2 10 4
0 0 0 0 0 0 1 1 1 0
1 1 1 0 0 0 0 0 0 0
'''