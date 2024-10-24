import sys
import math
def solve() :
    N = int(sys.stdin.readline())
    numbers = {}
    start = (0,0)
    getGAUDist = lambda x, y : math.sqrt(math.pow((x[0]-y[0]), 2) + math.pow((x[1] - y[1]), 2))
    
    for i in range(N) :
        u, v = map(int, sys.stdin.readline().split())
        numbers[(u, v)] = i # 각 좌표마다 번호를 부여한다.
        if i == 0 :
            start = (u, v)
    
    DP = [[-1 for _ in range(1<<N)] for _ in range(N)]
    
    def DFS(vertex, pattern) :
        if(pattern == (2**N) - 1) :
            return getGAUDist(vertex, start)
        
        if DP[numbers[vertex]][pattern] != -1 :
            return DP[numbers[vertex]][pattern]
        
        temp = float('inf')
        for nv, num in numbers.items() :
            if (1 << num) & pattern == 0 :
                temp = min(temp, DFS(nv, pattern | (1 << num)) + getGAUDist(vertex, nv))
        DP[numbers[vertex]][pattern] = temp
        
        return DP[numbers[vertex]][pattern]
    print('{0:0.9f}'.format(DFS(start, 1)))
solve()