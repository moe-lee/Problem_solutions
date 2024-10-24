import sys

def solve() :
    T, W = map(int, sys.stdin.readline().split())
    DP = [[[0, 0, 0] for _ in range(W+1)] for _ in range(T)]
    plums = [int(sys.stdin.readline()) for _ in range(T)]
    # F(k, w, i) = Max[F(k-1, w, i), F(k-1, w-1, (i+1) % 2)] + I[Plums[k] == i]
    if plums[0] == 1 : DP[0][0][1] = 1
    else : DP[0][1][2] = 1
    for p in range(1, len(plums)) :
        for w in range(W, 0, -1) :
            DP[p][w][1] = max(DP[p-1][w][1], DP[p-1][w-1][2]) + (1 if plums[p] == 1 else 0)
            DP[p][w][2] = max(DP[p-1][w][2], DP[p-1][w-1][1]) + (1 if plums[p] == 2 else 0)
        DP[p][0][1] = DP[p-1][0][1] + (1 if plums[p] == 1 else 0)
    tot_max = 0
    for i in range(W+1) :
        tot_max = max(tot_max, max(DP[T-1][i]))
    print(tot_max)
solve()

'''
test #1 :
5 1
1
1
1
1
1

'''