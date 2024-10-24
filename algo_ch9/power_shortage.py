import sys

def solve() :
    while True :
        m, n = map(int, sys.stdin.readline().split())
        if (m,n) == (0,0) : return
        edges = []
        max_cost = 0
        for _ in range(n) :
            u, v, z = map(int, sys.stdin.readline().split())
            max_cost += z
            edges.append((u, v, z))
        
        parent = [i for i in range(m)]
        rank = [1 for _ in range(m)]
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
        edges.sort(key = lambda x : -1 * x[2])
        num_of_groups = m
        total_profit = 0
        while edges and num_of_groups > 1 :
            u, v, c = edges.pop()
            if find(u) == find(v) : continue
            union(u, v)
            num_of_groups -= 1
            total_profit += c
        print(max_cost - total_profit)
solve()