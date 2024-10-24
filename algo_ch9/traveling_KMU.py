import sys

def formSpanningTree(N, first_edges, second_edges) :
    num_of_groups = N + 1
    parent = [i for i in range(N + 1)]
    rank = [1 for _ in range(N + 1)]
    def find(x) :
        if parent[x] != x :
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y) :
        xp, yp = find(x), find(y)
        if rank[xp] > rank[yp] :
            parent[yp] = xp
            rank[xp] += rank[yp]
        else :
            parent[xp] = yp
            rank[yp] += rank[xp]
    
    first_cnt = 0
    second_cnt = 0
    def generateTree(edges, num_of_groups) :
        num_of_edges = 0
        while edges and num_of_groups > 1:
            u, v = edges.pop()
            if find(u) == find(v) : continue
            union(u, v)
            num_of_edges += 1
            num_of_groups -= 1
        return num_of_edges, num_of_groups
    
    first_cnt, num_of_groups = generateTree(first_edges, num_of_groups)
    second_cnt, num_of_groups = generateTree(second_edges, num_of_groups)
    return (first_cnt, second_cnt)

def solve() : # 0번 부터 N번 건물까지 (N+1개)
    N, M = map(int, sys.stdin.readline().split())
    edges = { 0 : [], 1 : []}
    for _ in range(M+1) :
        u, v, c = map(int, sys.stdin.readline().split())
        edges[c].append((u, v))
    max_cost = formSpanningTree(N, edges[0][:], edges[1][:])[0] ** 2
    min_cost = formSpanningTree(N, edges[1][:], edges[0][:])[1] ** 2
    print(max_cost - min_cost)
solve()