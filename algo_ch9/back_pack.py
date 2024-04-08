import sys

n, k = list(map(int, sys.stdin.readline().split()))
backpack = [0 for i in range(k+1)]
#backpack = [[0 for j in range(k+1)] for s in range(n+1)]
items = [[0,0]]
for i in range(n) :
    # index 0 : weight, index 1 : wealth
    items.append(list(map(int, sys.stdin.readline().split())))

for j in range(1, n + 1) :
    for s in range(k, items[j][0] - 1, -1) :
        if s == items[j][0] or backpack[s - items[j][0]] :
            backpack[s] = max(backpack[s - items[j][0]] + items[j][1], backpack[s])
print(max(backpack))
