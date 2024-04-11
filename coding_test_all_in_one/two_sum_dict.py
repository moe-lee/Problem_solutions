def solve(nums, target) :
    memory = dict()
    for p in nums :
        if target - p in memory :
            return True
        else :
            memory[p] = True
    return False