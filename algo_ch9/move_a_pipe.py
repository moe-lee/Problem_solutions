n = int(input())
grid = [[0 for _ in range(n+1)]]
for _ in range(n): grid.append([0] + list(map(int, input().split())))
DP = [[[0, 0, 0] for _ in range(n+1)] for _ in range(n+1)] # 가로 대각 세로
DP[1][2][0] = 1
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if grid[i][j] == 1 : continue
        DP[i][j][0] += DP[i][j-1][0] + DP[i][j-1][1]
        DP[i][j][2] += DP[i-1][j][1] + DP[i-1][j][2]
        if grid[i-1][j] + grid[i][j-1] > 0 : continue
        DP[i][j][1] += sum(DP[i-1][j-1])
print(sum(DP[n][n]))