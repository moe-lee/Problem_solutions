import sys
import bisect
# 1차 시도. 이진 탐색 이용 - 시간초과
def solve() :
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    s.sort()
    if s[n-1] <= 0 :
        print(s[-2], s[-1])
        return

    if s[0] >= 0 :
        print(s[0], s[1])
        return    
    
    acid = bisect.bisect_left(s, 0)

    zero_sum = []
    for i in range(acid) :
        k = bisect.bisect_left(s[acid:], abs(s[i]))
        zero_sum.append([i,acid + k - 1,s[i] + s[acid + k - 1]])
    zero_sum = sorted(zero_sum, key= lambda x : x[2])

    i = bisect.bisect(zero_sum, 0, key= lambda x: x[2])
    print(s[zero_sum[i-1][0]], s[zero_sum[i-1][1]])

solve()