import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for _ in range(N-1) :
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parent_node = [0 for _ in range(N+1)]
depth = [0 for _ in range(N+1)]

q = deque()
visited = [False] * (N+1)
q.append((1, 0))
while q :
    p = q.popleft()
    visited[p[0]] = True
    for c in tree[p[0]] :
        if not visited[c] :
            parent_node[c] = p[0]
            depth[c] = p[1] + 1
            q.append((c, p[1] + 1))

M = int(sys.stdin.readline())
for _ in range(M) :
    A, B = map(int ,sys.stdin.readline().split())
    da, db = depth[A], depth[B]
    while da != db :
        if da > db :
            A = parent_node[A]
            da -= 1
        else :
            B = parent_node[B]
            db -= 1

    while A != B :
        A = parent_node[A]
        B = parent_node[B]
    print(A)
