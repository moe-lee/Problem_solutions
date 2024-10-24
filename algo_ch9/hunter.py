M, N, L = map(int, input().split())
ranges = list(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(N)]
ranges.sort()

def getDist(hunter, animal) :
    return abs(hunter - animal[0]) + animal[1]

animal_cnt = 0
for animal in animals :
    # 동물과 가장 가까운 사로를 찾는다.
    left, right = 0, M
    while left < right :
        mid = (left + right) // 2
        if ranges[mid] <= animal[0] :
            left = mid + 1
        else :
            right = mid
    dist = getDist(ranges[left - 1], animal)
    if left < M : dist = min(dist, getDist(ranges[left] ,animal))
    if dist <= L : 
        animal_cnt += 1
print(animal_cnt)