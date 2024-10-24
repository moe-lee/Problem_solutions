import sys
import heapq
from collections import defaultdict
def solve() :
    while(True) :
        N, M = map(int, sys.stdin.readline().split())
        if(N, M) == (0,0) : return
        S, D = map(int, sys.stdin.readline().split())
        
        graph = defaultdict(list)
        for _ in range(M) :
            u, v, p = map(int, sys.stdin.readline().split())
            graph[u].append((v, p))
        
        pq = [(0, S, -1)]
        sp_edges = [set() for _ in range(N)]
        costs = {}
        precedes = [[] for _ in range(N)]
        
        while pq :
            cur_cost, cur_vertex, prec = heapq.heappop(pq)
            if cur_vertex not in costs or cur_cost == costs[cur_vertex] :
                precedes[cur_vertex].append(prec)
            if cur_vertex not in costs :
                costs[cur_vertex] = cur_cost    
                if cur_vertex == D : continue
                for next_vertex, edge_cost in graph[cur_vertex]:
                    if next_vertex not in costs :
                        heapq.heappush(pq, (cur_cost + edge_cost, next_vertex, cur_vertex))
                    elif cur_cost + edge_cost == costs[next_vertex] :
                        precedes[next_v].append(cur_vertex)
        del_edges = []
        visited = [False] * (N+1)
        for prec in precedes[D] :
            del_edges.append((prec, D))
        while del_edges :
            from_v, to_v = del_edges.pop()
            sp_edges[from_v].add(to_v)
            if from_v == S or visited[from_v] : continue
            for prec in precedes[from_v] :
                del_edges.append((prec, from_v))
            visited[from_v] = True
        pq = [(0, S)]
        almost_min_cost = {}
        while pq :
            cur_cost, cur_vertex = heapq.heappop(pq)
            if cur_vertex not in almost_min_cost :
                almost_min_cost[cur_vertex] = cur_cost
                if cur_vertex == D : break
                for next_v, ec in graph[cur_vertex] :
                    if next_v not in almost_min_cost and next_v not in sp_edges[cur_vertex] :
                        heapq.heappush(pq, (cur_cost + ec, next_v))
        if D in almost_min_cost : print(almost_min_cost[D])
        else : print(-1)
solve()

'''
5 6
0 2
0 1 1
1 2 2
0 3 3
3 4 2
4 3 1
4 2 1


'''