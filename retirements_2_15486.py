# import sys
# N = int(sys.stdin.readline())
# # input form : (T_i, P_i)
# schedule = []
# for _ in range(N) :
#     t, p = map(int, sys.stdin.readline().split())
#     schedule.append((t, p))
# dp = [[0 for _ in range(51)] for _ in range(N)]
# for i in range(N) :
#     for j in range(50) : dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
#     dp[i][50] = 0
#     ti, pi = schedule[i]
#     dp[i][ti] = max(pi + dp[i][0], dp[i][ti])
# print(max(dp[N-1][0], dp[N-1][1]))

import sys

N = int(sys.stdin.readline())
schedule = []
for _ in range(N) :
    t, p = map(int ,sys.stdin.readline().split())
    schedule.append((t, p))

dp = [0] * (N + 1)
for i in range(N) :
    t_i, p_i = schedule[i]
    dp[i] = max(dp[i], dp[i-1])
    if i + t_i <= N :
        dp[i+t_i] = max(dp[i+t_i], dp[i] + p_i)
print(max(dp[N], dp[N-1]))