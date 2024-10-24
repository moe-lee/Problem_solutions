import sys

def solve() :
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    parent = [i for i in range(N + 1)]
    rank = [0] * (N+1)
    
    def find(x) :
        if parent[x] != x : 
            parent[x] = find(parent[x])
            return parent[x]
        else : return x
    
    def union(x, y) :
        x_rep, y_rep = find(x), find(y)
        if rank[x_rep] >= rank[y_rep] :
            parent[y_rep] = x_rep
        else :
            parent[x_rep] = y_rep
    
    edges = []
    for _ in range(M) :
        u, v, c = map(int, sys.stdin.readline().split())
        edges.append((c, u, v))
    edges.sort()
    min_cost = 0
    for edge in edges :
        c, u, v = edge
        if find(u) == find(v) : continue
        union(u, v)
        min_cost += c
    print(min_cost)
solve()