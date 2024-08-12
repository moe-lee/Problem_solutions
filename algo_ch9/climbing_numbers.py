import sys

def solve2_memo() :
    N = int(sys.stdin.readline())
    memo = {}
    def DFS(n, k) :
        if (n == N) : return 1
        if (n, k) not in memo :
            ans = 0
            for i in range(k, 10) :
                ans += DFS(n+1, i)
            memo[(n,k)] = ans % 10007
        return memo[(n,k)] % 10007
    print(DFS(-1, 0))

def solve() :
    N = int(sys.stdin.readline())
    ans = [[0 for _ in range(10)] for _ in range(N)]
    ans[0] = [1 for _ in range(10)]
    for i in range(1, N) :
        for j in range(10) :
            ans[i][j] = sum(ans[i-1][:j+1]) % 10007
    print(sum(ans[N-1])% 10007)
solve2_memo()
solve()