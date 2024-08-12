import sys

def solve() :
    n, m = map(int ,sys.stdin.readline().split())
    mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    # O(n*n) -> 10^6
    for i in range(n) :
        for j in range(1, n) :
            mat[j][i] += mat[j-1][i]
    for i in range(n) :
        for j in range(1, n) :
            mat[i][j] += mat[i][j-1]
    
    for _ in range(m) :
        r1, c1, r2, c2 = map(int ,sys.stdin.readline().split())
        ans = mat[r2-1][c2-1]
        scnt = 0
        if c1 - 2 >= 0 :
            ans -= mat[r2 - 1][c1 - 2]
            scnt += 1
        if r1 - 2 >= 0 :
            ans -= mat[r1 - 2][c2 - 1]
            scnt += 1
        if scnt == 2 :
            ans += mat[r1 - 2][c1 - 2]
        print(ans)
    return
solve()