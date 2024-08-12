import sys

def solve() :
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    for i in range(1, N) :
        j = i - 1
        while j >= i // 2 :
            prices[i] = max(prices[i], prices[j] + prices[(i-1) - j])
            j -= 1
    print(prices[N-1])
solve()