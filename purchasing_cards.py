import sys

def solve() :
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    for i in range(1, N) :
        for j in range(i-1, -1, -1) :
            cards[i] = min(cards[i], cards[j] + cards[i-1-j])
    print(cards[N-1])
solve()