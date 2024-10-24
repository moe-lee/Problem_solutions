import sys

def solve() :
    N, K = map(int, sys.stdin.readline().split())
    items = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    weights = [-1 for _ in range(K+1)]
    weights[0] = 0
    for w, v in items :
        for i in range(K, -1, -1) :
            if weights[i] != -1 and i + w <= K :
                weights[i+w] = max(weights[i+w], weights[i] + v)
    print(max(weights))
solve()