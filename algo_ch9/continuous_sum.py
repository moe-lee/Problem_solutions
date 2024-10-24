n = int(input())
nums = list(map(int, input().split()))
DP = [[-float('inf'), -float('inf')] for _ in range(n)]
DP[0][0] = nums[0]
for i in range(1, n) :
    DP[i][0] = max(DP[i-1][0] + nums[i], nums[i]) # 음수일 수 있으므로
    DP[i][1] = max(DP[i-1][1] + nums[i], DP[i-1][0])
max_sum = -float('inf')
for i in range(n) :
    max_sum = max(max_sum, max(DP[i]))
print(max_sum)