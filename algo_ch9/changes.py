import sys
tbl = [-1] * 100001
tbl[0] = -1
tbl[1] = -1
tbl[2] = 1
tbl[3] = -1
tbl[4] = 2
tbl[5] = 1
for i in range(6, 100001) :
    k = 999 if tbl[i-2] == -1 else tbl[i-2] + 1
    j = 999 if tbl[i-5] == -1 else tbl[i-5] + 1
    
    if k == 999 and j == 999 :
        tbl[i] = -1
    else :
        tbl[i] = min(k, j)

n = int(sys.stdin.readline())
print(tbl[n])