import sys

def solve() :
    N = int(sys.stdin.readline())
    weights = list(map(int, sys.stdin.readline().split()))
    max_weight = sum(weights)
    M = int(sys.stdin.readline())
    beads = list(map(int, sys.stdin.readline().split()))
    for bead in beads :
        DP = [[False for _ in range(40001)] for _ in range(2)]
        DP[0][bead] = True
        DP[1][0] = True
        flag = False
        for w in weights :
            for i in range(40000 - w, -1, -1) :
                if DP[1][i]:
                    DP[1][i+w] = True
                if DP[1][i+w] and DP[0][i+w] :
                    print('Y', end = " ")
                    flag = True
                    break
            if flag:
                break
            for i in range(40000 - w, -1, -1) :
                if DP[0][i] :
                    DP[0][i+w] = True
        if not flag :
            print('N', end = " ")
    return

def solve2() :
    n=int(input())
    l1=list(map(int,input().split()))
    m=int(input())
    l2=list(map(int,input().split()))

    dp={l1[0]} # set 생성
    for i in range(1,n):
        s={l1[i]} # 무게추들을 조합하여 만들수 있는 무게 + 어떤 조합에서 어떤 무게 추를 반대편에 놓음으로써 만들어지는 상대 무게
        for j in dp:
            s.add(j+l1[i])
            s.add(abs(j-l1[i]))
        dp=dp|s

    print(*map(lambda x:('Y' if x in dp else 'N'),l2)) # unpacking
solve2()
