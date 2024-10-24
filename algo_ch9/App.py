import sys

def solve() :
    N, M = map(int, sys.stdin.readline().split())
    DP = [-1 for _ in range(10001)]
    mems = list(map(int, sys.stdin.readline().split()))
    costs = list(map(int, sys.stdin.readline().split()))
    DP[0] = 0
    for i in range(len(mems)) :
        for j in range(10000, -1, -1) :
            if DP[j] != -1 and j + costs[i] <= 10000:
                DP[j + costs[i]] = max(DP[j+costs[i]], DP[j] + mems[i])
    min_cost = float('inf')
    for i in range(10000, -1, -1) :
        if DP[i] >= M :
            min_cost = i
    print(min_cost)
solve()

'''
5 5
1 1 1 1 1
10 10 10 10 10

3 10
5 5 10
1 1 0

5 100
20 20 20 20 20
0 0 0 0 0


test #1 : 중복 갱신
2 10
5
1
'''