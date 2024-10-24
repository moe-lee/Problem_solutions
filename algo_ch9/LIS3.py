import bisect
n = int(input())
A = list(map(int, input().split()))
DP = [0 for _ in range(n)]
DP[0] = 0
memo = [A[0]]
for i in range(1, n) :
    left, right = -1, len(memo) - 1
    while left < right :
        mid = (left + right) // 2 + 1
        if memo[mid] >= A[i] :
            right = mid - 1
        else :
            left = mid
    if right + 1 >= len(memo) :
        memo.append(A[i])
    else :
        memo[right+1] = A[i]
    DP[i] = right + 1
print(max(DP) + 1)

'''
3
3 2 1 

'''