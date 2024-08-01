def floydWashall(graph, V) :
    # graph는 초기 distance matrix를 초기화하는 과정에서 필요하다.
    # 이후 재귀연산은 distance matrix를 이용하여 수행한다.
    dist = [[None for _ in range(V + 1)] for _ in range(V + 1)]
    for i in range(1, V+1) :
        for cost, vertex in graph[i] :
            dist[i][vertex] = cost
    
    for k in range(1, V+1) :
        for i in range(1, V+1) :
            for j in range(1, V+1) :
                # shortestPath(i, j, K-1) = dist[i][j]
                # shortestPath(i, K, K-1) = dist[i][k]
                # shortestPath(K, j, K-1) = dist[k][j]
                if dist[i][j] is None :
                    if dist[i][k] is not None and dist[k][j] is not None :
                        dist[i][j] = dist[i][k] + dist[k][j]
                elif dist[i][k] is not None and dist[k][j] is not None :


                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(dist)

def floydWashallEx(graph, n) :
    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1) :
        for c in graph[i] :
            dist[i][c[1]] =c[0]
    
    for k in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(dist)

graph = [ [],
[(-2, 3)], [(4, 1), (3, 3)], [(2, 4)], [(-1, 2)] ]
floydWashall(graph=graph, V=4)