n = int(input())
carrages = list(map(int, input().split()))
L = int(input())
partail_sum = sum(carrages[0:L])
DP= [[0, 0, 0] for _ in range(n)]
DP[L-1][0] = partail_sum
for i in range(L, n) :
    partail_sum = partail_sum - carrages[i - L] + carrages[i]
    DP[i][0] = max(DP[i-1][0], partail_sum)
    if i-L >= L - 1: 
        DP[i][1] = max(DP[i-1][1], DP[i-L][0] + partail_sum)
        DP[i][2] = max(DP[i-1][2], DP[i-L][1] + partail_sum)
print(DP[n-1][2])