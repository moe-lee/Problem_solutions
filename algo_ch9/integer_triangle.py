import sys

n = int(sys.stdin.readline())
t = []
for i in range(n) :
    t.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n) :
    for j in range(i+1) :
        l = 0 if j == 0 else t[i-1][j-1]
        r = 0 if j == i else t[i-1][j]
        t[i][j] = max(l, r) + t[i][j]

print(max(t[n-1]))