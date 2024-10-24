import sys

def solve() :
    n, k = map(int, sys.stdin.readline().split())
    DP = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(k) : # sf(i, j, 0)
        u, v = map(int, sys.stdin.readline().split())
        DP[u][v] = 1
    
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if i == j : continue
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
    s = int(sys.stdin.readline().strip())
    
    for _ in range(s) :
        u, v = map(int, sys.stdin.readline().split())
        if DP[u][v] != float('inf') : print(-1)
        elif DP[v][u] != float('inf') : print(1)
        else : print(0)
    return
solve()