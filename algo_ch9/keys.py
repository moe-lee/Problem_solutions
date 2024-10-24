import sys
from collections import deque

def getKeyPos(alpha) :
    return ord(alpha.upper()) - 0x41

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    for i in range(N) :
        if grid[i][0] != '*' : 
            queue.append((i, 0))
            visited[i][0] = True
        if grid[i][M-1] != '*' : 
            queue.append((i, M-1))
            visited[i][M-1] = True
    for i in range(M) :
        if grid[0][i] != '*' and not visited[0][i]: 
            queue.append((0, i))
            visited[0][i] = True
        if grid[N-1][i] != '*' and not visited[N-1][i]: 
            queue.append((N-1, i))
            visited[N-1][i] = True
    key_holder = 0
    keys = sys.stdin.readline().strip()
    if keys != '0' :
        for key in keys :
            key_holder |= (1 << getKeyPos(key))
    
    step = ((-1, 0), (1, 0), (0, -1), (0, 1))
    doors = deque()
    doc_cnt = 0
    key_buff = key_holder
    while queue :
        cr, cc = queue.popleft()
        if 'A' <= grid[cr][cc] <= 'Z' and key_holder & (1 << getKeyPos(grid[cr][cc])) == 0 :
                doors.append((cr, cc))
        else :
            if 'a' <= grid[cr][cc] <= 'z' :
                key_holder |= (1 << getKeyPos(grid[cr][cc]))
            if grid[cr][cc] == '$' :
                doc_cnt += 1
            for sr, sc in step :
                nr, nc = cr + sr, cc + sc
                if 0<=nr<N and 0<=nc<M and grid[nr][nc] != '*' and not visited[nr][nc] :
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        if not queue :
            if key_buff == key_holder : break
            queue = doors
            doors = deque()
            key_buff = key_holder
    print(doc_cnt)
T = int(sys.stdin.readline())
for test_case in range(1, T+1) :
    solve()


'''
1
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz

1
5 11
*Y*********
*...*YYY*x*
*X*.*Y*Y*.*
*$*...*$*.y
***********
0

1
2 8
$******$
********
abaabaa
'''