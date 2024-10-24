import sys

def solve() :
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    DP = [[0 for _ in range(N+1)] for _ in range(K+1)]
    DP_RED = [[0 for _ in range(N+1)] for _ in range(K+1)]
    DP_RED[1][1] = 1
    for i in range(1, N+1) : DP[1][i] = 1
    for i in range(2, K+1) :
        for j in range(1, N+1) :
            if j - 2 >= 0 : 
                DP[i][j] = (DP[i-1][j-2] + DP[i][j-1]) % 1000000003
                DP_RED[i][j] = (DP_RED[i-1][j-2] + DP_RED[i][j-1]) % 1000000003
            if j == N :
                DP[i][j] -= DP_RED[i][j]
    print(sum(DP[K]) % 1000000003 )
solve()