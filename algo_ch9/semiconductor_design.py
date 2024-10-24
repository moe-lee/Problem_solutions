import bisect
import sys
def solve() :
    N = int(sys.stdin.readline())
    ports = list(map(int, sys.stdin.readline().split()))
    subseq = []
    ans = [0] * (N)
    for i in range(N) :
        idx = bisect.bisect_right(subseq, ports[i])
        ans[i] = idx + 1
        if len(subseq) == idx : subseq.append(ports[i])
        else : subseq[idx] = ports[i]
    
    print(max(ans))
solve()