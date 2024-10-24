import sys
def solve() :
    N, S, M = map(int, sys.stdin.readline().split())
    V = list(map(int, sys.stdin.readline().split()))
    def DFS(S, i) :
        if i == N:
            return S
        else :
            low = DFS((S - V[i]), i + 1) if S - V[i] >= 0 else -1
            high = DFS((S + V[i]), i + 1 )if S + V[i] <= M else -1
            if low == high and high == -1 :
                return -1
            return max(low, high)
    print(DFS(S, 0))
solve()

50
831 927 541 808 248 320 762 719 900 109 415 614 611 50 300 194 72 545 137 157 996 880 490 561 457 95 928 264 790 23 48 920 319 913 10 34 975 94 604 697 743 985 442 300 901 141 906 706 121 625