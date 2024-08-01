def twoSum(nums, target) :
    num_set = set()
    for n in nums :
        if (target - n) in num_set :
            return True
        num_set.add(n)
    return False

print(twoSum(nums=[2,1,5,7], target=14))