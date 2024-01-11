import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

tbl = []
for i in range(len(x)) :
    tbl.append([x[i], i, 0])
tbl = sorted(tbl,key=lambda x : x[0])

for i in range(1, len(tbl)) :
    if tbl[i][0] != tbl[i-1][0] :
        tbl[i][2] = tbl[i-1][2] + 1
    else :
        tbl[i][2] = tbl[i-1][2]

tbl = sorted(tbl, key = lambda x :x[1])
for i in tbl :
    print(i[2], end=" ")