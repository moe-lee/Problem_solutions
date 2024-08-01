def longestConsecutiveSequence(nums) :
    memo = dict()
    max_len = 0
    for n in nums :
        memo[n] = n+1
    for n in nums :
        if n-1 not in memo :
            st = n
            while st in memo : st = memo[st]
            max_len = max(st - n, max_len)
    return max_len

def demo1(nums) :
    num_set = dict()
    max_len = 0
    for num in nums :
        num_set[num] = True
    for num in nums :
        if num - 1 not in num_set :
            cnt = 1
            while num + cnt in nums :
                cnt += 1
            max_len = max(cnt, max_len)
    return max_len

def demo2(nums) :
    nums.sort()
    max_len = 0
    i = 0
    while i < len(nums) :
        cnt = 1
        j = i
        while j < len(nums) and (nums[j] <= nums[i] + cnt) :
            if nums[j] == nums[i] + cnt : cnt += 1
            j += 1
        max_len = max(max_len, cnt)
        i = j
    return max_len

#print(longestConsecutiveSequence(nums=[100,4,200,1,3,2]))
print(demo2(nums=[0,3,7,2,5,8,4,6,0,1]))
