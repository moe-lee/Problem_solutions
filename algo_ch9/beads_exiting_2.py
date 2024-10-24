import sys
import math
from collections import deque

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    queue = deque()
    step = ((0, 0), (-1, 0), (0, -1), (1, 0), (0, 1))
    red, blue = None, None
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 'B' :
                blue = [i, j, 'B']
            elif board[i][j] == 'R' :
                red = [i, j, 'R']
    queue.append((red, blue, 0))
    
    def declineBoard(cbead, sr, sc, other) :
        while 0<=(cbead[0] + sr)<N and 0<=(cbead[1] + sc)<M :
                if board[cbead[0] + sr][cbead[1] + sc] == '#': break
                if (cbead[0] + sr,cbead[1] + sc) == (other[0], other[1]) : break
                cbead[0], cbead[1] = cbead[0] + sr, cbead[1] + sc
                if board[cbead[0]][cbead[1]] == 'O' :
                    return True
        return False
    
    while queue :
        pfirst, psecond, cmove = queue.popleft()
        for direction in range(1, 5) :
            if cmove != 0 and cmove % 10 == direction : continue
            elif cmove != 0 and ((cmove % 10 - 1) + 2) % 4 + 1 == direction : continue
            cfirst = min(pfirst[:], psecond[:]) # 두 구슬이 겹칠 일은 없다.
            csecond = max(pfirst[:], psecond[:])
            if direction > 2 :
                cfirst, csecond = csecond, cfirst
            flag = {'R' : False, 'B' : False}
            
            sr, sc = step[direction]
            flag[cfirst[2]] = declineBoard(cfirst, sr, sc, (-1, -1))
            if flag[cfirst[2]] : cfirst[0], cfirst[1] = -1, -1
            flag[csecond[2]] = declineBoard(csecond, sr, sc, cfirst)
            if cmove < 10 ** 9 :
                if not any(flag.values()):
                    queue.append((cfirst, csecond, cmove * 10 + direction))
                else :
                    if flag['R'] and not flag['B']:
                        print(int(math.log10(cmove * 10 + direction)) + 1)
                        return
    print(-1)
solve()

'''
4 5
....O
.#.##
R#B..
#####

4 7
##...##
#..#.##
#R#O.B.
#..####

7 10
R.#...#B##
#...#.#.##
#####.#.##
#.....#.#.
#.#####.#.
#.O.......
#########.

3 1
.
B
R
'''