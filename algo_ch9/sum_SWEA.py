for _ in range(10) :
    t_num = input()
    nums = [list(map(int, input().split())) for _ in range(100)]
    ver_sum, hor_sum = [0]*(100), [0]*(100)
    dig_sum1, dig_sum2 = 0, 0
    for i in range(100) :
        for j in range(100) :
            if i == j :
                dig_sum1 += nums[i][j]
                dig_sum2 += nums[99 - i][j]
            ver_sum[i] += nums[i][j]
            hor_sum[j] += nums[i][j]
    print('#'+t_num, max([dig_sum1, dig_sum2, max(ver_sum), max(hor_sum)]))