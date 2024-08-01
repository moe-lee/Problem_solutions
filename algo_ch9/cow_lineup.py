import sys

def solve() :
    breeds_in_range = {}
    total_IDs = 0
    counting_set = set()
    N = int(sys.stdin.readline())
    cows = []
    for _ in range(N) :
        cows.append(tuple(map(int, sys.stdin.readline().split())))
        if cows[-1][1] not in counting_set : 
            counting_set.add(cows[-1][1])
            total_IDs += 1 # 총 품종 갯수 세기
    cows.sort(key=lambda x : x[0]) # 위치에 따라 정렬
    left, right = 0, 0
    photo_size = sys.maxsize
    
    while (left < right or right == 0):
        if len(breeds_in_range.keys()) < total_IDs and right < N: # 아직 모든 품종이 범위에 들어오지 않았다.
            _, breed = cows[right]
            if breed not in breeds_in_range :
                breeds_in_range[breed] = 0
            breeds_in_range[breed] += 1
            right += 1
        else :
            left_pos, left_breed = cows[left]
            right_pos, right_breed = cows[right - 1]
            if len(breeds_in_range.keys()) == total_IDs :
                photo_size = min(photo_size, right_pos - left_pos)
                breeds_in_range[left_breed] -= 1
                if breeds_in_range[left_breed] == 0 :
                    breeds_in_range.pop(left_breed)
            left += 1
    print(photo_size)
solve()