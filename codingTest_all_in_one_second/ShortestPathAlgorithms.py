import heapq

# Dijkstra O(|E|log|V|)
def dijkstra(graph, start, final, n) :
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))
    while pq :
        cur_cost, cur_vertex = heapq.heappop(pq)
        if cur_vertex not in costs :
            costs[cur_vertex] = cur_cost
            for cost, next_vertex in graph[cur_vertex] :
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_vertex))
    for i in range(1, n+1) :
        if i not in costs :
            return -1
    return costs[final]

# Bellman-Ford O(|V||E|)
def bellmanFord(edges, start, final, n) :
    costs = {}
    costs[start] = 0
    for _ in range(n) :
        for u, v, w in edges :
            # 무한대를 처리하는 것에 주의한다.
            if u in costs and v in costs and costs[u] + w < costs[v] :
                costs[v] = costs[u] + w
            elif u in costs and v not in costs :
                costs[v] = costs[u] + w
    # 음수 사이클
    for u, v, w in edges :
        if costs[u] + w < costs[v] :
            return None
    return costs[final]

# Floyd-Washall O(|V|^3)
def floydWashall(graph, n) :
    dist = [[None for _ in range(n + 1)] for _ in range(n+1)]
    for i in range(1, n+1) :
        for w, v in graph[i] :
            dist[i][v] = w
    
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                # shortestPath(i, j, k) = min(shortestPath(i,j,k-1), shortestPath(i,k,k-1) + shortestPath(k,j,k-1))
                if dist[i][j] is not None and dist[i][k] is not None and dist[k][j] is not None :
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                elif dist[i][k] is not None and dist[k][j] is not None :
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

bellmanFord(edges=[[0, 1, 6], [0, 2, 7], [1, 2, 8], [1, 3, 5], [1, 4, -4],
                   [2, 3, -3], [2, 4, 9], [3, 1, -2], [4, 0, 2], [4, 3, 7]], start=0, final=2, n=5)