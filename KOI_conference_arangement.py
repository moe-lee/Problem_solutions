import sys
def solve() :
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    DP = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N + 1) :
        DP[i][i] = 0
    for _ in range(M) : # shortestPath(i, j, 0)
        u, v = map(int, sys.stdin.readline().split())
        DP[u][v] = 1
        DP[v][u] = 1
    ## Floyd washall algorithm
    for k in range(1, N+1) :
        for i in range(1, N+1) :
            for j in range(1, N+1) :
                # shortestPath(i,j,k) = min[shortestPath(i,j,k-1), shortestPath(i, k, k-1)+shortestPath(k, j, k-1)]
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[j][k])
    #Direct Address를 이용하여 각 콜로니 탐색하기 + 대표 노드 버퍼에 저장하기. -> 해싱을 사용
    visited = [False] * (N+1)
    delegates = []
    colonies = 0
    for i in range(1, N+1) :
        if not visited[i] :
            colonies += 1
            neighbors = []
            min_max = [float('inf'), i]
            for j in range(1, N+1) :
                if DP[i][j] != float('inf') :
                    neighbors.append(j)
            while neighbors :
                cur_v = neighbors.pop()
                visited[cur_v] = True
                tmp_m = -1
                for k in range(1, N+1) :
                    if DP[cur_v][k] != float('inf') and DP[cur_v][k] > tmp_m :
                        tmp_m = DP[cur_v][k]
                if min_max[0] > tmp_m : min_max[0], min_max[1] = tmp_m, cur_v
            delegates.append(min_max[1])
    delegates.sort()
    print(colonies)
    for d in delegates : print(d)
solve()