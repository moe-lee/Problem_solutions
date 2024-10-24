import sys
from collections import deque

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    incline_to = ((0,0), (-1, 0), (0, -1), (1, 0), (0, 1))
    blue = None
    red = None
    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 'B' :
                blue = ((i, j))
            elif grid[i][j] == 'R' :
                red = ((i, j))
    queue = deque()
    queue.append(([*red, "r"], [*blue, "b"], 0))
    while queue :
        cfirst, csecond, cdir = queue.popleft() # 큐에 저장할 것 : 같은 순간의 Red, Blue의 위치, 움직인 방향모음
        for incline_idx in range(1, 5) :
            if cdir % 10 == incline_idx or cdir % 10 == ((incline_idx - 3) + 4) % 4 + 1 : # 마지막 방향의 반대 방향 or 같은 방향은 생략
                continue
            ir, ic = incline_to[incline_idx]
            ndir = cdir * 10 + incline_idx
            first, second = None, None
            flag = { 'r' : False, 'b' : False }
            first = min(cfirst[:], csecond[:])
            second = max(cfirst[:], csecond[:])
            if incline_idx >= 3 :
                first, second = second, first
            while 0<= first[0]+ir <N and 0<= first[1]+ic <M and grid[first[0]+ir][first[1]+ic] != '#' :
                first[0], first[1] = first[0] + ir, first[1] + ic
                if grid[first[0]][first[1]] == 'O':
                    flag[first[2]] = True
                    first[0] = -1
                    first[1] = -1
                    break
            
            while 0<= second[0]+ir <N and 0<= second[1]+ic <M and grid[second[0]+ir][second[1]+ic] != '#' and (second[0]+ir, second[1]+ic) != (first[0], first[1]):
                second[0], second[1] = second[0] + ir, second[1] + ic
                if grid[second[0]][second[1]] == 'O':
                    flag[second[2]] = True
            if flag['r'] and not flag['b'] :
                print(1)
                return
            elif not flag['b'] and ndir < 1000000000 :
                queue.append(([first[0], first[1], first[2]], [second[0], second[1], second[2]], ndir))
    print(0)
solve()
'''
test #1 : 
....O
.#.##
R#B..
#####
#####

ans = 1
'''

# blue를 먼저 BFS 시켜서 O에 도달 가능한 모든 경로를 set에 저장
    # Red를 BFS 시켜 O에 도달 시 set을 확인. 없다면? 성공.
    # 반복 횟수는 코너 당 4 ^ 10 번 => 10^6 정도
    # 불가능 :빨간 구슬과 파란 구슬은 겹쳐질 수 없다.
    
    # 동시에 움직일 경우 완전 동일한 기울임 패턴이 다음 칸에 있다면.. B,R이 겹쳐짐을 의미.
    # 아니라면 상관 없는 것 같음. => 모든 칸에 set이 필요하다?
    # 따로따로하면 Red가 먼저 인지 blue가 먼저인지 결정이 어렵다.
    # 동시에 움직여야 한다.
    