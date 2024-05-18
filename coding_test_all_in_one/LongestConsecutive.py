def longestConsecutive(nums) :
    longest = 0
    num_dict = set(nums)
    for num in nums :
        if num - 1 not in num_dict :
            cnt = 0
            target = num
            while target in num_dict :
                cnt += 1
                target += 1
            longest = max(cnt, longest)
    return longest


print(longestConsecutive([6,7,100,5,4,4]))

