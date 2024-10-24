import sys

def solve() :
    N = int(sys.stdin.readline())
    edges = []
    parent = [i for i in range(N+1)]
    rank = [1] * (N+1)
    
    def find(x) :
        if parent[x] != x :
            parent[x] = find(parent[x])
            return parent[x]
        else : return x
    
    def union(x, y) :
        p_x, p_y = find(x), find(y)
        if rank[p_x] > rank[p_y] : 
            parent[p_y] = p_x
            rank[p_x] += rank[p_y]
        else : 
            parent[p_x] = p_y
            rank[p_y] += rank[p_x]
        
    for i in range(1, N+1) :
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(i+1, N+1) :
            edges.append((i, j, line[j-1]))
    edges.sort(key = lambda x : -1 * x[2])
    num_of_groups = N
    tot_cost = 0
    while num_of_groups > 1:
        u, v, c = edges.pop()
        if find(u) == find(v) : continue
        union(u, v)
        tot_cost += c
        num_of_groups -= 1
    print(tot_cost)
solve()