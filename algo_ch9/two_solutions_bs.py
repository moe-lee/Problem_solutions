n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
min_diff_pair = [float('inf'), 0]

for i in range(len(solutions) - 1) :
    left, right = i+1, n
    while left < right :
        mid = (left + right) // 2
        if -solutions[i] >= solutions[mid] :
            left = mid + 1
        else :
            right = mid
    t = left - 1
    if t == i or (left < n and abs(solutions[t] + solutions[i]) > abs(solutions[left] + solutions[i])) :
        t = left
    if abs(solutions[i] + solutions[t]) < abs(sum(min_diff_pair)) :
        min_diff_pair = [solutions[i], solutions[t]]
print(*min_diff_pair)