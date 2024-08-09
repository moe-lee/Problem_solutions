import sys

def solve() :
    c = int(sys.stdin.readline())
    for _ in range(c) :
        N, L = map(int, sys.stdin.readline().split())
        costs = list(map(int, sys.stdin.readline().split()))
        min_avg = sys.maxsize
        for i in range(N - L + 1) :
            tsum = 0
            for j in range(i, N) :
                tsum += costs[j]
                if j - i >= L - 1 : min_avg = min(min_avg, tsum / (j - i + 1))
        print('%.10f'%(min_avg))

solve()