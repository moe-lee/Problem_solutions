import sys
from collections import defaultdict
from collections import deque

def BFS(forbidden, N, graph, match) :
    visited = 0
    queue = deque()
    for i in range(1, N+1) :
        if forbidden & (1 << (i-1)) == 0 :
            queue.append(i)
            visited |= (1 << (i-1))
            break
    while queue :
        cv = queue.popleft()
        if visited == match : return True
        for nv in graph[cv] :
            if ((forbidden | visited) & (1 << (nv - 1))) == 0 :
                visited |= (1 << (nv - 1))
                queue.append(nv)
    return False if visited != match else True

def solve() :
    # 입력 처리
    N = int(sys.stdin.readline())
    # 구역 별 비트 마스킹하여 인구수 저장, 유효X시 -1 저장
    DP = [float('inf') for _ in range(1<<10)]
    DP[0] = 0
    valid = [False] * (1<<N)
    cost = list(map(int, sys.stdin.readline().split()))
    total_population = sum(cost)
    
    graph = defaultdict(list)
    for i in range(1, N+1) :
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(1, len(line)) : graph[i].append(line[j])
    
    queue = deque()
    visited = [False] * (N+1)
    visited[1] = True
    queue.append(1)
    while queue :
        cv= queue.popleft()
        for i in range((1<<N) - 1, -1, -1) :
            if DP[i] != float('inf') :
                if i | (1 << (cv-1)) == 27 :
                    pass
                valid[i | (1 << (cv-1))] = BFS(i | (1 << (cv-1)), N, graph, (1<<N) - 1 - (i | (1 << (cv-1)))) and BFS((1<<N) - 1 - (i | (1 << (cv-1))), N, graph, i | (1 << (cv-1)))       
                DP[i | (1 << (cv-1))] = DP[i] + cost[cv-1]
        
        for nv in graph[cv] :
            if not visited[nv] : 
                visited[nv] = True
                queue.append(nv)
    
    min_diff = float('inf')
    for i in range(1, (1<<N) - 1) : # 연산자 우선순위 + 1구역 0, 2구역 a일때 전체 구역값과 차이가 같음.
        if DP[i] != float('inf') and valid[i]:
            min_diff = min(min_diff, abs((total_population - DP[i]) - DP[i]))
    print(min_diff if min_diff != float('inf') else -1)
    return
solve()

'''
5
1 1 1 1 1
0
3 3 4 5
1 2
1 2
1 2
ans = 3

9
1 1 1 1 1 1 1 1 1
2 2 3
2 1 3
2 1 2
2 5 6
2 4 6
2 4 5
2 8 9
2 7 9
2 7 8
ans = -1

6
3 3 3 3 3 3
1 2
2 1 3
3 2 4 6
2 3 5
1 4
1 3
ans : 6

3
1 2 3
1 2
1 1
0
ans = 0

5
1 1 10 1 1
4 2 3 4 5
4 1 3 4 5
4 1 2 4 5
4 1 2 3 5
4 1 2 3 4
ans = 6

5
0 0 3 0 0
3 2 4 5
1 1
0
1 1
1 1
ans : 3
'''