N = int(input())
requirements = list(map(int, input().split()))
budget = int(input())
left, right = 0, max(requirements) + 1
while left < right :
    mid = (left + right) // 2
    assigned_budget = 0
    for requirement in requirements :
        if assigned_budget > budget : break
        assigned_budget += min(requirement, mid)
    if assigned_budget <= budget : left = mid + 1
    else : right = mid
print(left - 1)