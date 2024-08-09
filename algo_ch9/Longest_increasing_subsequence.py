import sys

def solve() :
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    ans = A[:]
    max_v = A[0]
    for i in range(N) :
        j = i - 1
        max_sub_seq = 0
        while j >= 0 :
            if A[j] < A[i] : max_sub_seq = max(max_sub_seq, ans[j])
            j -= 1
        ans[i] += max_sub_seq
        max_v = max(max_v, ans[i])
    print(max_v)
    return
solve()

'''
6
100 200 300 400 200 1000

'''