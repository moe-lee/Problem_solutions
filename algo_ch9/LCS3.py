import sys
def LCS(s1, s2) :
    DP = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1) :
        for j in range(1, len(s2) + 1) :
            if s1[i-1] == s2[j-1] :
                DP[i][j] = DP[i-1][j-1] + 1
            else :
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    print(DP[-1][-1])
    return

def LCS3(s1, s2, s3) :
    DP = [[[0 for _ in range(len(s3) + 1)] for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    
    for i in range(1, len(s1) + 1) :
        for j in range(1, len(s2) + 1) :
            for k in range(1, len(s3) + 1) :
                if s1[i-1] == s2[j-1] == s3[k-1] :
                    DP[i][j][k] = DP[i-1][j-1][k-1] + 1
                else :
                    DP[i][j][k] = max(DP[i][j-1][k], DP[i-1][j][k], DP[i][j][k-1])
    print(DP[-1][-1][-1])
s1, s2, s3 = list(sys.stdin.readline().strip()), list(sys.stdin.readline().strip()),  list(sys.stdin.readline().strip())
LCS3(s1, s2, s3)

'''
abcedfg
abcdeg
abceg

오답 : 4
정답 : 5
'''