import sys

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    gender = [0]
    gender.extend(sys.stdin.readline().split())
    edges = []
    for _ in range(M) :
        u, v, d = map(int, sys.stdin.readline().split())
        if gender[u] == gender[v] : continue
        edges.append((u, v, d))
    edges.sort(key=lambda x : x[2] * -1)
    parent = [i for i in range(N+1)]
    rank = [1 for _ in range(N+1)]
    def find(x) :
        if parent[x] != x :
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y) :
        xp, yp = find(x),find(y)
        if rank[xp] > rank[yp] :
            parent[yp] = xp
            rank[xp] += rank[yp]
        else :
            parent[xp] = yp
            rank[yp] += rank[xp]
    num_of_group = N
    tot_dist = 0
    while num_of_group > 1 and edges:
        u, v, c = edges.pop()
        if find(u) == find(v) : continue
        tot_dist += c
        union(u, v)
        num_of_group -= 1
    print(tot_dist if num_of_group == 1 else -1)
solve()