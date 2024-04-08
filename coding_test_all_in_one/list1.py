import sys
# 1 2 3 4 5 6 7 9

def solve(nums, target) :
    nums.sort()
    i = 0
    j = len(nums) - 1
    while(i != j) :
        if(nums[i] + nums[j] > target) :
            j -= 1
        elif nums[i] + nums[j] < target :
            i += 1
        else :
            return True
    return False

print(solve([4, 1, 9, 7, 5, 3, 16], 14))