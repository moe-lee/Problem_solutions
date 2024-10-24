D, K = map(int, input().split())
DP = [[0, 0] for _ in range(D+1)]
DP[1] = [1, 0]
DP[2] = [0, 1]
for i in range(3, D+1) :
    DP[i] = [DP[i-1][0] + DP[i-2][0], DP[i-1][1] + DP[i-2][1]]
for i in range(1, 100001) :
    if (K - i * DP[D][0]) % DP[D][1] == 0 :
        print(i)
        print((K - i * DP[D][0]) // DP[D][1])
        break
