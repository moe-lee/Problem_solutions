import sys
# 1차 시도. 이진 탐색 이용 - 시간초과
# 입력으로 0이 들어오지 않는다.
def solve() :
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    s.sort()
    
    res = [0, n-1, s[0] + s[-1]]
    alkali = 0
    acid = n- 1
    while alkali < acid :
        if abs(res[2]) >= abs(s[acid] + s[alkali]) :
            res[0], res[1], res[2] = alkali, acid, s[alkali] + s[acid]
        if abs(s[alkali]) > abs(s[acid]) :
            alkali +=1
        else :
            acid -= 1
    print(s[res[0]], s[res[1]])

solve()

'''
3
-1 1 4
-1 4
1 4
-> -1, 1이 안나옴
'''