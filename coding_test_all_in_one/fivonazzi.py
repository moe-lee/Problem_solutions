memo = {}

def fibo(n) :
    if n == 0 or n == 1:
        return n
    if n not in memo :
        memo[n] = fibo(n-1) + fibo(n-1)
    return memo[n]

def fibo2(n) :
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1) :
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]