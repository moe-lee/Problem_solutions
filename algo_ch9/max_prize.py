def listToNumber(list) :
    ans = 0
    for n in list :
        ans *= 10
        ans += n
    return ans

T = int(input())
for test_case in range(1, T+1) :
    tokens = input().split()
    number = list(map(int, list(tokens[0])))
    C = int(tokens[1])
    DP = [[[[] for _ in range(len(number))] for _ in range(len(number))] for _ in range(C + 1)]
    for i in range(len(number)) :
        for j in range(len(number)) :
            DP[0][i][j] = number[:]
    for c in range(1, C+1) :
        for i in range(0, len(number) - 1) :
            for j in range(i+1, len(number)) :
                for k in range(0, len(number)) :
                    for p in range(0, len(number)) :
                        if k == p : continue
                        num = DP[c-1][k][p][:]
                        num[i], num[j] = num[j], num[i]
                        if listToNumber(DP[c][i][j]) < listToNumber(num) :
                            DP[c][i][j] = num[:]
                            DP[c][j][i] = num[:]
                
    max_prize = 0
    for i in range(0, len(number)) :
        for j in range(0, len(number)) :
            if(i == j) : continue
            max_prize = max(max_prize, listToNumber(DP[C][i][j]))
    print('#'+str(test_case), max_prize)
'''
1
32888 2
'''