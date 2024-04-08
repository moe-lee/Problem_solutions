import sys
import math

def solve() :
    G = int(sys.stdin.readline())
    C = int((G + 1) / 2)
    M = C - 1
    res = []
    
    while(C > 0 and M > 0) :
        if(C ** 2 - M ** 2 > G) :
            C -= 1
        elif(C ** 2 - M ** 2 < G) :
            M -= 1
        else :
            res.append(C)
            C -= 1
        if(C == M) : 
            M -=1
        
    if(res) :
        for i in range(1, len(res) + 1) :
            print(res[-1 * i])
    else :
        print(-1)
    return

if __name__ == '__main__' :
    solve()