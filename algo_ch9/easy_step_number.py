import sys
tbl = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

n = int(sys.stdin.readline())

for i in range(1, n) :
    tbl.append([0] * 10)
    tbl[i][0], tbl[i][9] = tbl[i-1][1], tbl[i-1][8]
    for j in range(1, 9) :
        tbl[i][j] = tbl[i-1][j-1] + tbl[i-1][j+1]

print(sum(tbl[n-1]))