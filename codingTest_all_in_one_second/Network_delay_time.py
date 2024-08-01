import heapq
from collections import defaultdict

def calculateMinimumDelayTime(times, n, k) :
    graph = defaultdict(list)
    for u, v, w in times :
        graph[u].append((w, v))
    
    costs = dict()
    pq = []
    heapq.heappush(pq,(0, k))
    while pq :
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs :
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v] :
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    
    for node in range(1, n + 1) :
        if node not in costs : return -1
    return max(costs.values())

print(calculateMinimumDelayTime(times=[[2,1,3],[2,3,5],[2,4,1],[4,3,3]], n=4, k=2))