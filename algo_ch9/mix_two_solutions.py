import sys

def solve() :
    n = int(sys.stdin.readline())
    solutions = list(map(int, sys.stdin.readline().split()))
    res = 1000000000
    l,r = 0, n - 1
    while(l < r) :
        if abs(solutions[l] + solutions[r]) < abs(res) :
            res = solutions[l] + solutions[r]
            if res == 0 : return 0
        if abs(solutions[l]) > abs(solutions[r]) :
            l += 1
        else :
            r -= 1
    return res

if __name__ == '__main__' :
    print(solve())