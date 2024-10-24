import sys
import bisect

def solve() :
    N = int(sys.stdin.readline())
    wires = [list(map(int ,sys.stdin.readline().split())) for _ in range(N)]
    wires.sort(key=lambda x : x[0])
    wired_port = []
    ans = [0] * (N)
    for k in range(0, N) :
        idx = bisect.bisect_right(wired_port, wires[k][1])
        if idx == len(wired_port) : wired_port.append(wires[k][1])
        else : wired_port[idx] = wires[k][1]
        ans[k] = idx + 1
    print(N-max(ans))
    return
solve()


'''
5
1 7
2 1
3 2
4 3
5 4
-> pass

5
1 5
2 4
3 3
4 2
5 1
-> pass

8
1 3
4 2
3 5
6 4
5 7
8 6
7 9
10 8
-> pass

5
3 1
1 2
5 3
2 4
4 5

'''