cost = []
memo = {}
def minCostCSTopDown(n) :
    if n == 0 or n == 1 :
        return 0
    if n not in memo :
        memo[n] = min(minCostCSTopDown(n-1) + cost[n-1], minCostCSTopDown(n-2) + cost[n-2])
    return memo[n]

def minCostCS(n) :
    memo = [0] * n
    for i in range(2, n) :
        memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
    return min(memo[n-1] + cost[n-1], memo[n-2] + cost[n-2])

print(minCostCS(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))