# 국경의 긴 터널을 빠져나오자, 눈의 고장이었다. 밤의 밑바닥이 하얘졌다. 신호소에 기차가 멈춰섰다.
def solve() :
    n = int(input())
    houses = []
    for i in range(0, n) :
        houses.append(list(map(lambda x : int(x), input().split())))
    
    costs = [[houses[0][0], houses[0][1], houses[0][2]]]
    for i in range(1, n) :
        costs.append([houses[i][0], houses[i][1], houses[i][2]])
        costs[i][0] = costs[i][0] + min(costs[i-1][1], costs[i-1][2])
        costs[i][1] = costs[i][1] + min(costs[i-1][0], costs[i-1][2])
        costs[i][2] = costs[i][2] + min(costs[i-1][0], costs[i-1][1])
    
    print(min(min(costs[n-1][0], costs[n-1][1]),costs[n-1][2]))


solve()

'''
3
1 2 3
1 1 3
8 1 8

0 0 1
1 1 1

0 2 1
1 3 1
'''