def topsort(graph) :
    N = len(graph)
    V = [False] * (N + 1)
    ordering = [0] * N
    i = N - 1
    
    for at in range(1, N+1) :
        if not V[at] :
            dfs(i, at, V, ordering, graph)
    return ordering

def dfs(i, at, V, ordering, graph) :
    V[at] = True
    for to in graph[at] :
        if not V[to] :
            i = dfs(i, to, V, ordering, graph)
    ordering[i] = at
    return i - 1



def dfs2(i, at, V, ordering, graph) :
    V[at] = True
    for nv in graph[at] :
        if V[nv] == False :
            i = dfs2(i, nv, V, ordering, graph)
    ordering[i] = at
    return i - 1

def topSort2(graph) :
    N = len(graph) - 1
    V = [False] * (N+1)
    ordering = [0] * (N)
    i = N - 1
    
    for at in range(1, N + 1) :
        if V[at] == False :
            i = dfs2(i, at, V, ordering, graph)
    return ordering

graph = [ [],
[2, 5], [3, 5], [], [5], [6], [], [4]
]

order = topSort2(graph)
print(order)