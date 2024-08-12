import sys
N = int(sys.stdin.readline())
nums = list(map(int ,sys.stdin.readline().split()))
max_num = nums[0]
for i in range(1, N) :
    nums[i] = max(nums[i-1] + nums[i], nums[i])
    max_num = max(max_num, nums[i])
print(max_num)