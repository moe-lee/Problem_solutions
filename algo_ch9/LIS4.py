import sys
import bisect

def solve() :
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    DP = [0] * (N)
    seq_momo = []
    for i in range(0, N) :
        index = i - 1
        lis_prev = -1
        while index >= 0 :
            if (A[index] < A[i]) :
                if lis_prev == - 1 or (DP[lis_prev] < DP[index]) :
                    lis_prev = index
            index -= 1
        if lis_prev == -1 : 
            DP[i] = 1
            seq_momo.append([A[i]])
        else : 
            DP[i] = DP[lis_prev] + 1
            nseq = seq_momo[lis_prev][:]
            nseq.append(A[i])
            seq_momo.append(nseq)
    max_idx = 0
    for i in range(0, N) :
        if DP[max_idx] < DP[i] :
            max_idx = i
    print(DP[max_idx])
    for s in seq_momo[max_idx] :
        print(s, end=" ")
solve()

'''
5
30 10 30 20 40 20
'''