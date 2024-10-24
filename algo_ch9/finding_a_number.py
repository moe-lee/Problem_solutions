# N = int(input())
# nums = list(map(int, input().split()))
# M = int(input())
# targets = list(map(int, input().split()))
# nums.sort()
# for target in targets :
#     left, right = 0, N-1
#     while left < right :
#         mid = (left + right) // 2
#         if nums[mid] < target :
#             left = mid + 1
#         else :
#             right = mid
#     res = 0
#     if nums[left] == target : res = 1
#     print(res)

N = int(input())
memo = set(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))
for t in targets :
    if t in memo : print(1)
    else : print(0)
