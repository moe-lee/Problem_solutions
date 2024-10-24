import sys
from collections import deque

step = ((-1, 0), (1, 0), (0, -1), (0, 1))

def solve() :
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[-1 for _ in range(N)] for _ in range(N)] # 거리를 저장하는 리스트 -1 == 미방문
    memo = [[0 for _ in range(N)] for _ in range(N)] # 섬 번호를 기록할 리스트 -> 동일 섬 출발, 동일 섬 도착 방지
    coast = deque()
    number_of_island = 2
    # 1차 BFS = 섬 스캔, 번호 부여 및 해안선 저장
    for i in range(N) :
        for j in range(N) :
            if grid[i][j] == 1 and visited[i][j] == -1 :
                queue =  deque()
                queue.append((i, j))
                visited[i][j] = 0
                memo[i][j] = number_of_island
                while queue :
                    cr, cc = queue.popleft()
                    for sr, sc in step :
                        nr, nc = cr + sr, cc + sc
                        if(0<= nr <N and 0<= nc <N) and visited[nr][nc] == -1 :
                            memo[nr][nc] = number_of_island
                            if grid[nr][nc] == 1 :
                                queue.append((nr, nc))
                                visited[nr][nc] = 0
                            else :
                                coast.append((nr, nc))
                                visited[nr][nc] = 1
                number_of_island += 1
    bridges = []
    while coast :
        cr, cc = coast.popleft()
        for sr, sc in step :
            nr, nc = cr + sr, cc + sc
            if (0<= nr <N and 0<= nc <N) :
                if visited[nr][nc] != -1 and memo[nr][nc] != memo[cr][cc] :
                    bridges.append((visited[nr][nc] + visited[cr][cc]))
                if visited[nr][nc] == -1 and grid[nr][nc] == 0 :
                    coast.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1
                    memo[nr][nc] = memo[cr][cc]
    print(min(bridges))
solve()


'''
4
1 0 0 1
1 0 0 1
1 0 1 0
1 0 0 0
'''