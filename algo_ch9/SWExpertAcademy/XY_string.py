T = int(input())
res = []
for testcase in range(1, T+1) :
    S = input()
    E = list(input())
    while len(E) > len(S) :
        poped = E.pop()
        if poped == 'Y' : E.reverse()
    flag = True
    for i in range(len(E)) :
        if E[i] != S[i] :
            flag = False
            break
    if flag : res.append('Yes')
    else : res.append('No')
for i in range(1, T+1) :
    print(f'#{i} {res[i-1]}')

'''
3
Y
XYYX
XY
XYY
X
YY
'''