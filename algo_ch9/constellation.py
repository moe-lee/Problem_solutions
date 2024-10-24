import sys
import math
def solve() :
    N = int(sys.stdin.readline())
    stars = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]
    edges = []
    for i in range(len(stars) - 1) :
        for j in range(i + 1, len(stars)) :
            dist = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
            edges.append((i, j, dist))
    edges.sort(key=lambda x : x[2] * -1)
    parent = [i for i in range(N)]
    rank = [1 for _ in range(N)]
    num_of_groups = N
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
    min_dist_sum = 0.0
    while num_of_groups > 1 :
        u, v, dist = edges.pop()
        if find(u) == find(v) : continue
        min_dist_sum += dist
        union(u, v)
        num_of_groups -= 1
    print('{0:.2f}'.format(min_dist_sum))
solve()