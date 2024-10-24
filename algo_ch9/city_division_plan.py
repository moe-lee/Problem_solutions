import sys

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    edges.sort(key=lambda x : -1 * x[2])
    parent = [ i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]
    num_of_groups = N
    tot_mt_fee = 0
    def find(x) :
        if x != parent[x] :
            parent[x] = find(parent[x])
            return parent[x]
        return x
    
    def union(x, y) :
        x_par, y_par = find(x), find(y)
        if rank[x_par] > rank[y_par] :
            parent[y_par] = parent[x_par]
            rank[x_par] += rank[y_par]
        else :
            parent[x_par] = parent[y_par]
            rank[y_par] += rank[x_par]
    while num_of_groups > 2:
        u, v, c = edges.pop()
        if find(u) == find(v) : continue
        tot_mt_fee += c
        num_of_groups -= 1
        union(u, v)
    print(tot_mt_fee)
solve()