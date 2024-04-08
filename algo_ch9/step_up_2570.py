import sys
n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(int(sys.stdin.readline()))

tbl = [[s[0], 0]]

for i in range(1, n) :
    t = [0, 0]
    t[0] = max(tbl[i-2][1] + s[i-1], tbl[i-2][0]) + s[i]
    t[1] = tbl[i-1][0]
    tbl.append(t)

print(tbl[n-1][0])
