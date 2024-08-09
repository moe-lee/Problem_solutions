import sys
def solve() :
    N = int(sys.stdin.readline())
    dp = [[[0 for _ in range(10)] for _ in range(100)] for _ in range(N)]
    for i in range(1, 10) :
        dp[0][i*10+i][i] = 1
    for i in range(N) :
        for left in range(0, 10) :
            for right in range(left, 10) :
                if(left - 1) >= 0 :
                    dp[i][(left-1) * 10 + right][left - 1] += (dp[i-1][(left * 10) + right][left]) % (1000000000)
                if(right + 1) < 10 :
                    dp[i][(left * 10) + (right + 1)][right + 1] += (dp[i-1][(left * 10) + right][right]) % (1000000000)
                for z in range(left, right + 1) :
                    if z - 1 >= left : dp[i][(left * 10) + right][z] += (dp[i-1][(left * 10) + right][z-1])
                    if z + 1 <= right : dp[i][(left * 10) + right][z] += (dp[i-1][(left * 10) + right][z+1])
                    dp[i][(left * 10) + right][z] %= 1000000000
    print(sum(dp[-1][9]) % (1000000000))
solve()