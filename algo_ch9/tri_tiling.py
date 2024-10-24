import sys

def solve() :
    N = int(sys.stdin.readline())
    tiling = [0 for _ in range(31)] # 단 N이 홀수 = 0
    pure = [2] * (31)
    pure[2] = 3
    tiling[2] = 3
    for i in range(4, 31) :
        for j in range(2, i, 2) :
            tiling[i] += pure[j] * tiling[i-j]
        tiling[i] += pure[i]
    print(tiling[N] if N % 2 == 0 else 0)
solve()