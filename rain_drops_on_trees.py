import sys
from collections import deque
def solve() :
    n, w = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1) :
        u, v = map(int,sys.stdin.readline().split())
        tree[u].append(v)
        tree[v].append(u)
    visited = [False for _ in range(n+1)]
    def bfs(root) :
        num_of_child = 0
        num_of_leaves = 0
        queue = deque()
        queue.append(root)
        visited[root] = True
        while queue :
            num_of_child = 0
            curr_vertex = queue.popleft()
            for v in tree[curr_vertex] :
                if not visited[v] :
                    num_of_child += 1
                    visited[v] = True
                    queue.append(v)
            if num_of_child == 0 :
                num_of_leaves += 1
        return num_of_leaves
    print(f'{w / bfs(1):.11}')
    return

solve()