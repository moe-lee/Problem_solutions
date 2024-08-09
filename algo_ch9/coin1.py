import sys

def solve() :
    N, K = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline()) for _ in range(N)]
    coins.sort()
    noc = [0] * (K+1)
    noc[0] = 1
    for coin in coins :
        for i in range(1, K+1) :
            if(i - coin >= 0) :
                noc[i] += noc[i-coin]
    print(noc[K])
    return
solve()