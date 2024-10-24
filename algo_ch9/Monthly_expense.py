n, m = map(int, input().split())
expense = [int(input()) for _ in range(n)]
left, right = max(expense) - 1, 10 ** 9
while left < right :
    mid = (left + right) // 2 + 1
    transaction_cnt = 1
    acc = mid
    for exp in expense :
        if transaction_cnt > m : break
        if acc - exp < 0 :
            transaction_cnt += 1
            acc = mid
        acc -= exp
    if transaction_cnt <= m :
        right = mid - 1
    else :
        left = mid
print(right + 1)