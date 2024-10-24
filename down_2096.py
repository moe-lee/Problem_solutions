import sys

def solve() :
    N = int(sys.stdin.readline())
    DP_max = [0, 0, 0]
    DP_min = [float('inf') for _ in range(3)]
    for i in range(N) :
        line = list(map(int ,sys.stdin.readline().split()))
        if i == 0 :
            DP_max = line
            DP_min = line
        else :
            tmp_max = [0, 0, 0]
            tmp_min = [float('inf') for _ in range(3)]
            for o in range(3) :
                for k in range(-1, 2) :
                    if 3> o + k >= 0 :
                        tmp_max[o] = max(tmp_max[o], DP_max[o+k])
                        tmp_min[o] = min(tmp_min[o], DP_min[o+k])
                tmp_max[o] += line[o]
                tmp_min[o] += line[o]
            DP_max = tmp_max
            DP_min = tmp_min
    print(max(DP_max), min(DP_min))
solve()