import sys
import heapq
from collections import deque

nums = list(sys.stdin.readline().strip())
N = len(nums)
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1) :
    DP[i][i] = 1
for i in range(1, N+1) :
    for j in range(1, N+1) :
        if j + i > N : break
        if nums[j-1] == nums[i+j - 1] :
            if i == 1:
                DP[j][j+i] = 1
            elif DP[j+1][j+i-1] > 0 :
                DP[j][j+i] = 1
visited = [float('inf') for _ in range(N+1)]
queue = []
for i in range(1, N+1) :
    if DP[1][i] != 0 :
        heapq.heappush(queue, (1, i + 1))
        visited[i] = 1
success = False
while queue :
    np, end = heapq.heappop(queue)
    if end == 29:
        pass
    if end == N + 1 :
        break
    for i in range(end, N+1) :
        if visited[i] == float('inf') and DP[end][i] != 0 :
            divided = True
            visited[i] = np + 1
            if i == N:
                success = True
                break
            heapq.heappush(queue, (np + 1, i + 1))
    if success : break

print(visited[N])

'''
BB C DD E C A E C B DABAD D C E B A CCC B D C A ABDBA DD
11 2 33 4 5 6 7 8 9 10  10 11 12 13 14 15 16 16  17
'''