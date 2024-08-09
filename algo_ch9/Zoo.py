import sys
sys.setrecursionlimit(1000000)
def solve() :
    N = int(input())
    lion = ((False, False), (True, False), (False, True))
    memo = dict()
    def zoo(n, l, r) :
        if n == 0 :
            return 1
        ans = 0
        for ll, lr in lion :
            if not ((ll and l) or (lr and r)) :
                if (n-1, ll, lr) not in memo :
                    memo[(n-1, ll, lr)] = zoo(n-1, ll, lr) % 9901
                ans += memo[(n-1, ll, lr)]
        return ans
    print(zoo(N, False, False)%9901)

import sys
def solve2() :
    N = int(sys.stdin.readline())
    memo = [[0,0,0] for _ in range(N+1)]
    memo[0] = (1, 1, 1)
    lions = ((False, False), (True, False), (False, True))
    for i in range(1, N+1) :
        memo[i][0] = (memo[i-1][0] + memo[i-1][1] + memo[i-1][2]) % 9901
        memo[i][1] = (memo[i-1][0] + memo[i-1][2]) % 9901
        memo[i][2] = (memo[i-1][0] + memo[i-1][1]) % 9901
    sys.stdout.write(str(memo[N][0]))
    return

solve2()