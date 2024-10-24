for test_case in range(1, 11) :
    t_num = int(input())
    nums = list(map(int, input().split()))
    offset = 15
    min_cycle = min(nums) // offset - 1
    reduction = 0
    for i in range(8) : nums[i] -= min_cycle * offset
    while nums[reduction % 8] - (reduction % 5 + 1) > 0 :
        nums[reduction % 8] -= (reduction % 5 + 1)
        reduction += 1
    nums[reduction % 8] = 0
    reduction += 1
    print('#'+str(test_case)+' ', end="")
    for i in range(8) :
        print(nums[(reduction + i)% 8], end=" ")