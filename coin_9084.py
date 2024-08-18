import sys

def solve() :
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins :
        for i in range(M+1) :
            if i - coin >= 0 :
                dp[i] += dp[i-coin]
    print(dp[M])

T = int(sys.stdin.readline())
for _ in range(T) :
    solve()