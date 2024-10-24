import sys
N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1) :
    DP[i][i] = 1
for i in range(1, N+1) :
    for j in range(1, N+1) :
        if j + i > N : break
        if nums[j-1] == nums[i+j - 1] :
            if i == 1:
                DP[j][j+i] = 1
            elif DP[j+1][j+i-1] == 1 :
                DP[j][j+i] = 1
M = int(sys.stdin.readline().strip())
for _ in range(M) :
    S, E = map(int, sys.stdin.readline().split())
    print(DP[min(S,E)][max(S,E)])

'''
7
1 1 3 4 3 2 1

'''
