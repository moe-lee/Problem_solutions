for test_case in range(1, 11) :
    dumps = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(dumps) :
        nums[-1] -= 1
        nums[0] += 1
        nums.sort()
    print('#'+str(test_case),nums[-1] - nums[0])