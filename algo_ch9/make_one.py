from collections import deque
x = int(input())
DP = {x : -1}
queue = deque()
queue.append((x, -1))
steps = 0
predicates = [lambda x : x % 3 == 0, lambda x : x % 2 == 0, lambda x : True]
opers = [lambda x : x // 3, lambda x : x // 2, lambda x : x - 1]
while queue :
    if 1 in DP : break
    nqueue = deque()
    for cx, cp in queue :
        for i in range(3) :
            next_pos = opers[i](cx)
            if next_pos not in DP and predicates[i](cx):
                DP[next_pos] = cx
                nqueue.append((next_pos, cx))
    steps += 1
    queue = nqueue
print(steps)
footprint = []
cur = 1
while cur != -1 :
    footprint.append(cur)
    cur = DP[cur]
footprint.reverse()
print(*footprint)
