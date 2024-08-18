import sys

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    dp = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    step = ((0, -1), (-1, -1), (-1, 0))
    memo = {}
    def backtrack(n, m) :
        if(n == m == 0) :
            return dp[n][m]
        candies = 0
        for sr, sc in step :
            nr, nc = n + sr, m + sc
            if(0<=nr<N and 0<=nc<M) :
                if (nr, nc) not in memo :
                    memo[(nr, nc)] = backtrack(nr, nc)
                candies = max(candies, memo[(nr, nc)])
        return candies + dp[n][m]
    print(backtrack(N-1, M-1))

import sys
def tabulate() :
    N, M = map(int, sys.stdin.readline().split())
    dp = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N) :
        for j in range(M) :
            tmp = 0
            if(0<=i-1<N and 0<=j-1<M) : tmp = max(tmp, dp[i-1][j-1])
            if(0<=i-1<N) : tmp = max(tmp, dp[i-1][j])
            if(0<=j-1<M) : tmp = max(tmp, dp[i][j-1])
            dp[i][j] += tmp
    print(dp[N-1][M-1])
solve()