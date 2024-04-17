import sys

def isNested(a, b) :
    if a[1] + b[1] < abs(a[0] - bp[0]) :
    
    return True

def solve() :
    N = int(input())
    circles = []
    for _ in range(N) :
        circles.append(tuple(map(int, sys.stdin.readline().split())))
    circles.sort(key= lambda x : x[1])
    
    stack = []
    
    
    print(circles)


if __name__ == '__main__' :
    solve()