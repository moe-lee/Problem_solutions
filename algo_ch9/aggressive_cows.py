N, C = map(int, input().split())
stalls = [int(input()) for _ in range(N)]
stalls.sort()
# 1. 백트래킹. 약 10만 팩토리얼 => impossible
# 2. N개의 stall 전부 사용 X, C마리를 배치해야함.
# 3. 1부터 차근 차근 해당 거리로 이격하여 배치가 가능한지 탐색.
# 4. 가능한 거리차이는 최대 10^9
# 5. 순차 탐색 시간복잡도 O(N) => 범위 값에 따라 배치 가능 소 마릿수는 정렬됨.
# 6. 이진 탐색 적용이 가능 O(log2(N)), 5,6번 에서 N은 최소 이격 거리
left, right = 1, 10**9 + 1
while left < right :
    mid = (left + right) // 2
    stored_cows = 1
    dist_acc = 0
    for i in range(1, len(stalls)) :
        if stored_cows > C : break
        dist_acc += stalls[i] - stalls[i-1]
        if dist_acc >= mid :
            stored_cows += 1
            dist_acc = 0
    if stored_cows >= C :
        left = mid + 1
    else :
        right = mid
print(left - 1)