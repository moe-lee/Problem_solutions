import sys

def solve() :
    N = int(sys.stdin.readline())
    wires = [0 for _ in range(501)]
    
    crossing = [[] for _ in range(501)]
    
    for _ in range(N) :
        u, v = map(int, sys.stdin.readline().split())
        wires[u] = v
    
    for i in range(1, 501) :
        for j in range(1, 501) :
            