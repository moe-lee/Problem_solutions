memo = {1 : 1, 2 : 2}
def climbingStairs(n) :
    for i in range(3, n + 1) :
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(climbingStairs(13))