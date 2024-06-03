import sys
from collections import deque
sys.setrecursionlimit(100000)

def bfs(tree, praise_cnt, root) :
    queue = deque()
    queue.append(root)
    visited = set()
    # 두 명 이상의 직속상사가 있을 경우를 고려함.
    while queue :
        cur_node = queue.popleft()
        if cur_node in visited :
            continue
        visited.add(cur_node)
        for v in tree[cur_node] :
            praise_cnt[v] += praise_cnt[cur_node]
            queue.append(v)

def solve() :
    n, m = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(n+1)]
    parents = tuple(map(int, sys.stdin.readline().split()))
    
    for i in range(1, len(parents)) :
        tree[parents[i]].append(i+1)
    
    praise_cnt = [0 for _ in range(n+1)]
    
    for _ in range(m) :
        senior_number, cnt = map(int, sys.stdin.readline().split())
        # 칭찬을 여러번 받을 경우를 고려해야한다.
        praise_cnt[senior_number] += cnt
    
    bfs(tree, praise_cnt, 1)
    for i in range(1, n+1) :
        print(praise_cnt[i], end=(' ' if i < n else ''))
    
    return

solve()