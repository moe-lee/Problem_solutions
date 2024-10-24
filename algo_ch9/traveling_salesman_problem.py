import sys

# 출발점을 고정한 뒤 풀어도 된다. -> 최소비용인 해밍턴 경로 : 모든 노드를 포함하고 있다.
def solve() :
    N = int(sys.stdin.readline())
    weights = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    total_min = sys.maxsize
    DP = [[dict() for _ in range(N)] for _ in range(N)]
    DP[0][0][1] = 0
    for j in range(N - 1) :
        for cv in range(N) :
            for patt, cost in DP[j][cv].items() :
                for nv in range(0, N) :
                    if cv != nv and weights[cv][nv] > 0 and (patt & (1 << nv)) == 0 :
                        DP[j+1][nv][patt | (1 << nv)] = min(DP[j+1][nv].get((patt | (1 << nv)), float('inf')), cost + weights[cv][nv])
    for k in range(N) :
        if k != 0 and (2**N - 1) in DP[N-1][k] and weights[k][0] :
            total_min = min(total_min, DP[N-1][k][2**N - 1] + weights[k][0])
    print(total_min)

def solve2() :
    N = int(sys.stdin.readline())
    weights = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    DP = [[ -1 for _ in range(1<<N)] for _ in range(N)]
    
    def DFS(patt, vertex) :
        if patt == (1<<N) - 1 :
            return weights[vertex][0] if weights[vertex][0] != 0 else float('inf')
        if DP[vertex][patt] != -1 : return DP[vertex][patt]
        
        DP[vertex][patt] = float('inf')
        for nv in range(1, N) :
            if weights[vertex][nv] != 0 and (patt & (1<<nv) == 0):
                DP[vertex][patt] = min(DP[vertex][patt], DFS(patt | (1 << nv), nv) + weights[vertex][nv])
        return DP[vertex][patt]
    print(DFS(1, 0))
    return
solve2()

'''
4
0 7 3 3
7 0 9 2
1 9 0 12
7 7 12 0
'''