import sys

def searchTarget(nums, target) :
    left = 0
    right = len(nums) - 1
    min_diff = sys.maxsize
    while left < right:
        min_diff = min(min_diff, abs(target - (nums[left] + nums[right])))
        if nums[left] + nums[right] < target :
            left += 1
        else :
            right -= 1
    return min_diff

def solve() :
    N = int(input())
    snow_balls = list(map(int, input().split()))
    snow_balls.sort()
    height_set = set() # hash set
    smallest_difference = sys.maxsize
    
    for right in range(N-1, 2, -1) :
        for left in range(0, right - 2) :
            h = snow_balls[left] + snow_balls[right]
            if h not in height_set :
                height_set.add(h)
                min_diff = searchTarget(snow_balls[left+1:right], h)
                smallest_difference = min(min_diff, smallest_difference)
                if not smallest_difference :
                    print(0)
                    return
    print(smallest_difference)
    return

'''
8
1 3 4 6 1325 8746 12566 8756254 
0
'''
solve()