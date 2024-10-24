# import sys
# import heapq
# N = int(sys.stdin.readline())
# grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# DP = [[[float('inf') for _ in range(201)] for _ in range(N)] for _ in range(N)] # N이 Upper bound, contained N, N이 Lower bound
# steps = ((-1, 0), (0, -1), (1, 0), (0, 1))
# # heap을 이용하는 것이 더 적합해 보인다.
# pq = [(0, grid[0][0], grid[0][0], 0, 0, -1)] # 차이, min, max, 좌표
# DP[0][0][grid[0][0]] = grid[0][0]
# while pq :
#     diff, min_sf, max_sf, cr, cc, prev = heapq.heappop(pq)
#     if (cr, cc) == (N-1, N-1) :
#         print(diff)
#         break
#     for idx in range(len(steps)) :
#         nr, nc = cr + steps[idx][0], cc + steps[idx][1]
#         if (0<= nr < N) and (0<= nc < N) and idx != prev:
#             min_sf_next = min(min_sf, grid[nr][nc])
#             max_sf_next = max(max_sf, grid[nr][nc])
#             if DP[nr][nc][min_sf_next] > max_sf_next :
#                 DP[nr][nc][min_sf_next] = max_sf_next
#                 heapq.heappush(pq, (max_sf_next - min_sf_next, min_sf_next, max_sf_next, nr, nc, (idx + 2) % 4))
'''
3
1 99 99
0 99 99
0 0 0

2
3 5
2 3

3
10 15 15
10 9 15
8 8 20

5
10 15 15 15 100
10 8 100 15 100
5 8 8 10 100
100 100 100 10 10
100 100 100 100 20


3
2 4 5
1 2 2
6 2 4
'''

import sys
from collections import deque
N = int(sys.stdin.readline())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
left = min(board[0][0], board[N-1][N-1])
ans = 201
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while left >= 0:
    right_s = max(board[0][0], board[N-1][N-1])
    right_e = 200
    temp = 0
    
    while right_s <= right_e:
        mid = (right_s+right_e)// 2
        visited = [[0]* N for _ in range(N)]
        queue = deque([[0, 0]])
        visited[0][0] = 1
        while queue:
            r, c = queue.popleft()
            if r == N-1 and c == N-1:
                temp = mid
                right_e = mid -1
                break
            for i in range(4):
                nr, nc = r+dx[i], c+dy[i]
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 and left <= board[nr][nc] <= mid:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
        else:
            right_s = mid + 1
    if temp:
        ans = min(ans, temp-left)
    left -= 1
print(ans)