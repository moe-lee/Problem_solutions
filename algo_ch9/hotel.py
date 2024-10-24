import sys

def solve() :
    C, N = map(int, sys.stdin.readline().split())
    popul_cost = [float('inf')] * 101
    max_popul = 0
    for _ in range(N) :
        c, n = map(int,sys.stdin.readline().split())
        max_popul = max(max_popul, n)
        popul_cost[n] = min(popul_cost[n], c)
    for c in range(max_popul - 1, 0, -1) :
        popul_cost[c] = min(popul_cost[c], popul_cost[c+1])
    DP = [float('inf') for _ in range(C+1)]
    DP[0] = 0
    for i in range(C+1) :
        for j in range(1, 101) :
            if i - j < 0 or popul_cost[j] == float:break
            DP[i] = min(DP[i], DP[i-j] + popul_cost[j])
    print(DP[C])
solve()