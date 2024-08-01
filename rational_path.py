import sys
from collections import deque

def solve() :
    n, m =map(int, sys.stdin.readline().split())
    tree = { 'main' : [] }
    for _ in range(n + m) :
        p, f, c = sys.stdin.readline().split()
        if p in tree :
            if f not in tree[p] :
                tree[p].append(f)
        else :
            tree[p] = [f]
        
        if c == '1' and f not in tree :
            tree[f] = []
    
    def BFS(root) :
        queue = deque()
        queue.append(root)
        history = dict()
        while queue :
            pwd = queue.popleft()
            for e in tree[pwd] :
                if e not in tree :
                    if e not in history :
                        history[e] = 0
                    history[e] += 1
                else :
                    queue.append(e)
        return (len(history.keys()), sum(history.values()))

    q = int(input())
    for _ in range(q) :
        path = sys.stdin.readline().strip().split('/')
        res = BFS(path[-1])
        print(res[0],res[1])
    
solve()