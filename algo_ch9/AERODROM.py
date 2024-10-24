N, M = map(int, input().split())
proc_time = [int(input()) for _ in range(N)]
proc_time.sort()
# 1초부터 10 ** 18 초 범위에서 M명처리 가능한 시간을 찾는다.
# 주의 : lower bound 찾기
left, right = 0, 10 ** 18
while left < right :
    mid = (left + right) // 2 + 1
    passed_men = 0
    for time in proc_time :
        if passed_men > M : break
        passed_men += mid // time
    if passed_men >= M :
        right = mid - 1
    else :
        left = mid
print(right + 1)
