def permutate(nums) :
    result = []
    def backtrack(curr) :
        if len(curr) == len(nums) :
            result.append(curr[:])
            return
        
        for num in nums :
            if num not in curr :
                curr.append(num)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return result

def combinate(nums, k) :
    result = []
    def backtrack(start, curr) :
        if len(curr) == k :
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)) :
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return result

def subsets(nums) :
    result = []
    
    def backtrack(start, curr) :
        if len(curr) == k :
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)) :
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    
    for k in range(0, len(nums)+1) :
        backtrack(0, [])
    return result

print(subsets(nums = [1,2,3,4]))