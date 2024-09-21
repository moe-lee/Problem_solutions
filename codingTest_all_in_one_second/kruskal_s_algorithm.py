from collections import defaultdict
parent = {}
rank = {}
for c in ('A','B','C','D','E','F','G','H','I','J') : 
    parent[c] = c
    rank[c] = 0

def find(x) :
    if parent[x] != x : return find(parent[x])
    return x

def union(x, y) :
    parent[find(y)] = find(x)

def kruskal(edges) :
    edges.sort(key=lambda x : x[2])
    mst = defaultdict(list)
    for u, v, c in edges :
        if find(u) == find(v) :
            continue
        mst[u].append((c, v))
        mst[v].append((c, u)) # non-directed graph
        union(u, v)
    print(mst)
edges = [('I','J', 0), ('C','H',4), ('A','E',1), ('G','I',4),
         ('C','I', 1), ('A','B',5), ('E','F',1), ('D','F',5),
         ('G','H', 1), ('H','I',6), ('B','D',2), ('F','G',7),
         ('C','J', 2), ('D','G',11), ('D','E',2), ('D','H',2),
         ('A','D', 4), ('B','C',4)]
kruskal(edges=edges)