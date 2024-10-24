# Binary search : seach upper bound
nums = # 정렬된 숫자의 리스트
target = # 탐색 대상
N = len(nums)
left, right = -1, N # 탐색 위치 정의
while left < right :
    mid = (left + right) // 2 + 1
    if nums[mid] >= target :
        right = mid - 1
    else :
        left = mid
print(right + 1)


N, M = map(int, input().split())
lectures = list(map(int, input().split()))
left, right = max(lectures) - 1, 10**9
while left < right :
    mid = (left + right) // 2 + 1
    num_of_dvd = 0
    acc = 0
    for lect in lectures :
        if acc + lect > mid :
            num_of_dvd += 1
            acc = 0
        acc += lect
    num_of_dvd += 1
    if num_of_dvd <= M :
        right = mid - 1
    else :
        left = mid
print(right + 1)

'''
5 5
1 2 3 4 5

'''