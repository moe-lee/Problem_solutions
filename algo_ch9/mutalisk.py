from collections import deque
N= int(input())
scv = list(map(int, input().split())) + [0 for _ in range(3-N)]
scv.sort()
UNVISITED = -1
DP = [[[UNVISITED for _ in range(61)] for _ in range(61)] for _ in range(61)]
step = [[0, 1, 2], [0, 2, 1], [1, 2, 0], [1, 0, 2], [2, 1, 0], [2, 0, 1]]
queue = deque()
queue.append([*scv])
DP[scv[0]][scv[1]][scv[2]] = 1
while queue :
    ca, cb, cc= queue.popleft()
    for sa, sb, sc in step :
        next_scv = [max(0, ca - 3**sa), max(0, cb - 3**sb), max(0, cc - 3**sc)]
        if all(map(lambda x : x == 0, next_scv)) :
            print(DP[ca][cb][cc])
            exit()
        next_scv.sort()
        if DP[next_scv[0]][next_scv[1]][next_scv[2]] == UNVISITED :
            DP[next_scv[0]][next_scv[1]][next_scv[2]] = DP[ca][cb][cc] + 1
            queue.append(next_scv)