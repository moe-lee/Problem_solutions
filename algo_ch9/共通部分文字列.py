import sys

def solve() :
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    DP = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1) :
        for j in range(1, len(B) + 1) :
            if A[i-1] == B[j-1] :
                DP[i][j] = max(DP[i][j], DP[i-1][j-1] + 1)
    ans = 0
    for l in DP: ans = max(ans, max(l))
    print(ans)
solve()