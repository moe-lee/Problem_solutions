import sys
from collections import deque
def BFS() :
    links = {   'D' : lambda x : (x * 2) % 10000,
                'S' : lambda x : (x - 1 + 10000) % 10000,
                'L' : lambda x : ((x // 1000) + (x % 1000 * 10)),
                'R' : lambda x : (x % 10) * 1000 + (x // 10)
            }
    queue = deque()
    visited = [False for _ in range(10000)]
    
    A, B = map(int, sys.stdin.readline().split())
    if A == B :
        print('')
        return
    visited[A] = True
    queue.append((A, ''))
    while queue :
        cur_regi, cur_cmd = queue.popleft()
        for cmd, link in links.items() :
            next_regi = link(cur_regi)
            if not visited[next_regi] :
                if next_regi == B :
                    print(cur_cmd + cmd)
                    return
                queue.append((next_regi, cur_cmd + cmd))
                visited[next_regi] = True
    return

def solve() :
    T = int(sys.stdin.readline())
    for _ in range(T) :
        BFS()
solve()