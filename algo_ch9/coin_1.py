import sys

def solve() :
    N, K = map(int, sys.stdin.readline().split())
    coins = []
    num_table = [0] * (K+1)
    for _ in range(N) :
        coins.append(int(sys.stdin.readline()))
        if coins[-1] <= K :
            num_table[coins[-1]] = 1
    
    for i in range(1, K+1) :
        for coin in coins :
            if i - coin >= 0 :
                num_table[i] += (num_table[i-coin])
    print(num_table[K])
solve()