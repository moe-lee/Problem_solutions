import heapq

def dijkstra(graph, start, final, n) :
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))
    while pq :
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs :
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v] :
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]

graph = {
    1: [(2,2), (1,4)],
    2: [(1,3), (9,5), (6,6)],
    3: [(4,6)],
    4: [(3,3), (5,7)],
    5: [(1,8)],
    6: [(3,5)],
    7: [(7,6), (9, 8)],
    8: []
}

print(dijkstra(graph=graph, start=1, final=8, n=8))