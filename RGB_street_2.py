import sys

def solve() :
    N = int(sys.stdin.readline())
    costs = [[0,0,0]]
    for _ in range(N) : costs.append(list(map(int, sys.stdin.readline().split())))
    ans = sys.maxsize
    def searchMinCost(firstColor) :
        min_costs = [[float('inf') for _ in range(3)] for _ in range(N+1)]
        min_costs[1][firstColor] = costs[1][firstColor]
        for i in range(2, N) :
            for j in range(3) :
                min_costs[i][j] = min(min_costs[i][j], min_costs[i-1][(j + 1) % 3] + costs[i][j])
                min_costs[i][j] = min(min_costs[i][j], min_costs[i-1][(j + 2) % 3] + costs[i][j])
        min_costs[N][(firstColor + 1) % 3] = min(min_costs[N-1][firstColor], min_costs[N-1][(firstColor + 2) % 3]) + costs[N][(firstColor + 1) % 3]
        min_costs[N][(firstColor + 2) % 3] = min(min_costs[N-1][firstColor], min_costs[N-1][(firstColor + 1) % 3]) + costs[N][(firstColor + 2) % 3]
        
        return min(min_costs[N])
    for i in range(3) :
        ans = min(ans, searchMinCost(i))
    print(ans)
solve()