import sys
def solve(N) :
    DP = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(2*N+1)]
    DP[0][0][N] = 1
    for i in range(0, 2*N) :
        for w in range(0, N+1) :
            for h in range(0, N+1) :
                if(w - 1 >= 0 and h + 1 < (N+1)) :
                    DP[i+1][h+1][w-1] += DP[i][h][w]
                if(h-1 >= 0) :
                    DP[i+1][h-1][w] += DP[i][h][w]
    print(DP[2*N][0][0])

while True :
    n = int(sys.stdin.readline().strip())
    if n == 0 : break
    solve(n)