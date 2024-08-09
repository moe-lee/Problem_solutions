import sys

def calcCost(src, dest) :
    if src == dest : return 1
    elif src == 0 : return 2
    elif abs(src - dest) == 2 : return 4
    else : return 3

def solve() :
    directions = list(map(int, sys.stdin.readline().split()))[:-1]
    dp = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(len(directions))]
    dp[0][directions[0]][0] = 2
    dp[0][0][directions[0]] = 2
    for i in range(1, len(directions)) :
        drt = directions[i]
        for j in range(0, 5) :
            if j == drt : continue
            for k in range(0, 5) :
                if j != k : dp[i][drt][j] = min(dp[i][drt][j], dp[i-1][k][j] + calcCost(k, drt))
        for j in range(0, 5) :
            if j == drt : continue
            for k in range(0, 5) :
                if j != k : dp[i][j][drt] = min(dp[i][j][drt], dp[i-1][j][k] + calcCost(k, drt))
    min_cost = float('inf')
    for i in range(5) :
        for j in range(5):
            min_cost = min(dp[-1][i][j], min_cost)
    print(min_cost)
solve()