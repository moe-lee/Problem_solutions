T = int(input())

def getNested(p1, p2) :
    # 만약 두 종이가 겹친다면? 두 종의 왼쪽 x좌표 중 더 큰 것 ><두 종이 오른쪽 x좌표 중 더 작은것
    if max(p1[0], p2[0]) < min(p1[2], p2[2]) :
        # and 두 종이 위쪽 y 좌표 중 더 작은것 > 두 종이 아랫쪽 y좌표 중 더 큰것
        if max(p1[1], p2[1]) < min(p1[3], p2[3]) :
            return (max(p1[0], p2[0]), max(p1[1], p2[1]), min(p1[2], p2[2]), min(p1[3], p2[3]))
    return None

for test_case in range(1, T+1) :
    wp = list(map(int, input().split()))
    bp1 = list(map(int, input().split()))
    bp2 = list(map(int, input().split()))
    area = (wp[2] - wp[0]) * (wp[3] - wp[1])
    np1 = getNested(wp, bp1)
    if np1 : area -= (np1[2] - np1[0]) * (np1[3] - np1[1])
    np2 = getNested(wp, bp2)
    bnp = getNested(bp1, bp2)
    if bnp : bnp = getNested(wp, bnp)
    reduction = 0
    if np2 : 
        reduction += (np2[2] - np2[0]) * (np2[3] - np2[1])
        if bnp : reduction -= (bnp[2] - bnp[0]) * (bnp[3] - bnp[1])
    if area - reduction > 0 : print('YES')
    else : print('NO')


'''
2
4 4 7 5
0 0 4 9
0 1 4 6
2 3 4 5
3 1 5 6
1 1 3 7

1
2 2 3 3
1 1 4 4
0 0 5 5


'''