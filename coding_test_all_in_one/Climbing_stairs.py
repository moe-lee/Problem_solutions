def climbingStairs(n) :
    list = [0 for _ in range(n+1)]
    list[0] = 1
    list[1] = 1
    for i in range(2, n+1) :
        list[i] = list[i-1] + list[i-2]
    print(sum(list[n]))
    return

climbingStairs(n=3)



memo = dict()
costs = []
def climbingstairs_1(n) :
    if(n <= 1) : return 0
    if n not in memo :
        memo[n] = climbingstairs_1(n-1) + climbingstairs_1(n-2)
    return memo[n]

def min_cost(n) :
    if(n <= 1) : return 0
    if n not in memo :
        memo[n] = min(min_cost(n-1) + costs[n-1], min_cost(n-2) + costs[n-2])
    return memo[n]

def min_cost_2(n) :
    memo[0] = memo[1] = 0
    for i in range(2, 8) :
        memo[i] = min(memo[i-1] + costs[i-1], memo[i-2] + costs[i-2])
    return memo[n]
min_cost(5) + costs[5]
