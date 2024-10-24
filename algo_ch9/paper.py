# import sys
# N, D = map(int, sys.stdin.readline().split())
# left, right = 1, N
# while left < right:
#     mid = (left + right) // 2
#     lines = mid
#     tmp = mid

#     while tmp > 0:
#         lines += tmp // D
#         tmp //= D

#     if lines < N:
#         left = mid + 1  # 목표보다 작은 경우 왼쪽 범위를 좁힘
#     else:
#         right = mid  # 목표를 찾았거나 넘은 경우 오른쪽 범위를 좁힘

# print(left)
n = int(input())
res = 1
for i in range(1, n+1) :
    res *= i
print(res)