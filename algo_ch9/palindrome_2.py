def searchPalin(string) :
    max_len = 1
    for j in range(0, 99) :
        palin_len = 0
        left, right = j, j+1
        if string[j] != string[right] : 
            palin_len +=1
            left = j-1
        while (0<=left and right<100) and string[left] == string[right] :
            palin_len += 2
            left -= 1
            right += 1
        max_len = max(max_len, palin_len)
    return max_len

for test_car in range(1,11) :
    t_num = input()
    grid_lat = [list(input()) for _ in range(100)]
    grid_lon = [['' for _ in range(100)] for _ in range(100)]
    for i in range(100) :
        for j in range(100) :
            grid_lon[i][j] = grid_lat[j][i]
    max_len = 1
    for i in range(100) :
        max_len = max(max_len, searchPalin(grid_lat[i]))
        max_len = max(max_len, searchPalin(grid_lon[i]))
    
    print('#'+t_num, max_len)