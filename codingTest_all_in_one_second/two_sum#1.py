# brute force.
def twoSumBruteForce(nums, target) :
    for i in range(len(nums)-1) :
        for j in range(i+1, len(nums)) :
            if nums[i] + nums[j] == target :
                return True
    return False

def twoSum(nums, target) :
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right :
        if nums[left] + nums[right] == target :
            return True
        elif nums[left] + nums[right] > target :
            right -= 1
        else :
            left += 1
    return False

print(twoSum(nums=[4,1,9,7,8,16], target=14))