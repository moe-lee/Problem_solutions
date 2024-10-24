n = int(input())
if n == 1 :
    print(1)
    exit()
DP = [0 for _ in range(n+1)]
DP[1] = 1
DP[2] = 2
for i in range(2, n+1) :
    DP[i] += DP[i-1] % 10007 + DP[i-2] % 10007 * 2
    DP[i] %= 10007
print(DP[n] % 10007)