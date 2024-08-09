import sys
from collections import deque

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    steps = ((-1, 0), (1, 0), (0, -1), (0, 1))
    shamt = {'a' : 1,'b' : 2, 'c' : 3,'d' : 4,'e' : 5,'f' : 6,'0' : 0}
    visited = [[set() for _ in range(M)] for _ in range(N)]
    grid = []
    queue = deque()
    for i in range(N) : # 미로 입력
        grid.append(list(sys.stdin.readline().strip()))
        for j in range(M) :
            if grid[i][j] == '0' :
                queue.append((i,j,0,['0']))
                visited[i][j].add(1)
    
    while queue :
        cr, cc, cd, ck = queue.popleft()
        if grid[cr][cc] == '1' : 
            print(cd)
            return
        for sr, sc in steps :
            nr, nc = cr + sr, cc + sc
            if 0<=nr<N and 0<=nc<M and grid[nr][nc] != '#':
                flag = 0
                for k in ck : flag |= (1 << shamt[k])
                if flag in visited[nr][nc] : continue
                # 다음 칸이 . 또는 소문자 또는 대문자
                nk = ck[:]
                if grid[nr][nc] != '0' and grid[nr][nc] in shamt and grid[nr][nc] not in ck: nk.append(grid[nr][nc])# 키 리스트는 복사해야함.
                elif grid[nr][nc].isalpha() and grid[nr][nc].lower() not in ck:
                    continue# 키목록에 해당 키가 없다면 continue
                queue.append((nr,nc, cd+1, nk))
                visited[nr][nc].add(flag)
    print(-1)
    return
solve()

'''
#1
6 6
a#AAA1
.#B###
.#A###
0.....
#####b
#####a


3 7
f0.F...
aF....A
b....B1


  A


'''