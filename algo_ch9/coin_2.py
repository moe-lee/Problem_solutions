import sys

def solve() :
    N, K = map(int, sys.stdin.readline().split())
    coins = set()
    for _ in range(N) :
        coins.add(int(sys.stdin.readline()))
    coins = list(coins)
    
    num_of_coins = [sys.maxsize] * (K+1)
    for cost in coins :
        if cost <= K :
            num_of_coins[cost] = 1
    
    for i in range(K+1) :
        for cost in coins :
            if i - cost >= 0 :
                num_of_coins[i] = min(num_of_coins[i], num_of_coins[i-cost] + 1)
    return num_of_coins[K] if num_of_coins[K] < sys.maxsize else -1

print(solve())