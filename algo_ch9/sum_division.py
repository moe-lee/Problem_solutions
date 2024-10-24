import sys

def solve() :
    N, K = map(int, sys.stdin.readline().split())
    DP = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
    for i in range(K+1) : DP[i][0] = 1
    for j in range(N+1) : DP[1][j] = 1
    for i in range(2, K+1) :
        acc = DP[i-1][0]
        for j in range(1, N+1) :
            acc = (acc + DP[i-1][j]) % (10 ** 9)
            DP[i][j] = acc 
    print(DP[K][N])
solve()