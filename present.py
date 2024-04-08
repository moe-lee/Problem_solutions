import sys

def solve() :
    N, D = tuple(map(int, sys.stdin.readline().split()))
    presents = []
    for _ in range(N) :
        presents.append(list(map(int, sys.stdin.readline().split())))
    presents.sort(key=(lambda a : a[0]))
    l, r, samax, tmp_sat = 0, 0, 0, 0
    
    while(r < N) :
        if(presents[r][0] - presents[l][0] < D) :
            tmp_sat += presents[r][1]
            r+=1
        else :
            samax = max(samax, tmp_sat)
            tmp_sat -= presents[l][1]
            l += 1
    samax = max(samax, tmp_sat)
    print(samax)


if __name__ == '__main__' :
    solve()