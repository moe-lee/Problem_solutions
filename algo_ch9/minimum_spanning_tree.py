import sys
sys.setrecursionlimit(10**5)
def solve() :
    V, E = map(int, sys.stdin.readline().split())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
    edges.sort(key = lambda x : x[2])
    total_weight = 0
    num_of_groups = V
    
    parent = [i for i in range(V+1)]
    rank = [0 for _ in range(V+1)]
    
    def find(x) :
        if x != parent[x] : return find(parent[x])
        else : return x
    
    def union(x, y) :
        x_rep = find(x)
        y_rep = find(y)
        if rank[x_rep] > rank[y_rep] :
            parent[y_rep] = x_rep
            rank[x_rep] += 1
        else :
            parent[x_rep] = y_rep
            rank[y_rep] += 1
    
    for u, v, c in edges :
        if num_of_groups == 1 : break
        if find(u) == find(v) : continue
        total_weight += c
        num_of_groups -= 1
        union(u, v)
    print(total_weight)
solve()