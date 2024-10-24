c,n = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(n)]
max_popul = 0
for i in costs : max_popul = max(max_popul, i[1])
DP = [float('inf') for _ in range(c+max_popul)]
DP[0] = 0
for i in range(1, c+max_popul) :
    for cost, popul in costs :
        if i - popul >= 0 :
            DP[i] = min(DP[i-popul] + cost, DP[i])
print(min(DP[c:c+max_popul]))