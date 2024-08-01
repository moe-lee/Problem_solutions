# 간선의 리스트가 전달된다. 각 엔트리는 (u : 출발노드, v : 도착노드, w : 가중치)로 구성됨.
def bellmanFord(edges, start, n) :
    dist = [None] * n # None is used as the INFINITY Token
    dist[start] = 0
    predecessor = [None] * n
    for i in range(n) :
        for u, v, w in edges :
            if dist[u] is not None :
                if dist[v] is None or dist[u] + w < dist[v] :
                    predecessor[v] = u
                    dist[v] = dist[u] + w
    
    for u, v, w in edges :
        if dist[u] + w < dist[v] :
            print("negative cycle detected")
    print(dist)


def bellmanFord44(edges, start, final, n) :
    costs = [float('inf')] * n
    costs[start] = 0
    for _ in range(n) :
        for u, v, w in edges :
            if costs[v] > costs[u] + w :
                costs[v] = costs[u] + w
    
    for u, v, w in edges :
        if costs[v] > costs[u] + w :
            raise Exception('음수 사이클')
    print(costs)
    return costs[final]

bellmanFord(edges=[[0, 1, 6], [0, 2, 7], [1, 2, 8], [1, 3, 5], [1, 4, -4],
                   [2, 3, -3], [2, 4, 9], [3, 1, -2], [4, 0, 2], [4, 3, 7]], start=0,n=5)