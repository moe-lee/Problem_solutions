def getPaindrome(string, limit) :
    validPalin = 0
    for i in range(0, 8 - limit + 1) :
        res = True
        for j in range(0, limit//2) :
            if string[i+j] != string[i+limit-1-j] :
                res = False
                break
        if res : validPalin += 1
    return validPalin

for test_case in range(1, 11) :
    lenth = int(input())
    grid_ver = [list(input()) for _ in range(8)]
    grid_hor = [['' for _ in range(8)] for _ in range(8)]
    for i in range(8) :
        for j in range(8) :
            grid_hor[i][j] = grid_ver[j][i]
    valid_pal = 0
    for i in range(8) :
        valid_pal += getPaindrome(grid_ver[i], lenth)
        valid_pal += getPaindrome(grid_hor[i], lenth)
    print('#'+str(test_case), valid_pal)