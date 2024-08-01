import sys

def solve() :
    N = int(sys.stdin.readline())
    grams = list(map(int, sys.stdin.readline().split()))
    
    def findClosestGroups(left) :
        bound = left+1
        left_group, right_group = grams[left], 0
        min_diff, max_grams = sys.maxsize, 0
        for i in range(left + 1, N) :
            right_group += grams[i]
            while(bound < i and abs(left_group - right_group) > abs(left_group + grams[bound] - (right_group - grams[bound]))) :
                left_group += grams[bound]
                right_group -= grams[bound]
                bound += 1
            
            if min_diff > abs(left_group - right_group) :
                min_diff = abs(left_group - right_group)
                max_grams = left_group + right_group
            elif min_diff == abs(left_group - right_group) :
                max_grams = max(max_grams, left_group + right_group)
        
        return (min_diff, max_grams)
    
    min_diff_so_far = sys.maxsize
    max_gram_so_far = 0
    
    # 좌 우에서 Sandwitch -> 100 200 1300 1000 1000 -> error
    # 모든 경우를 다 뒤져야 함 -> 랜덤하므로.
    # 중복되는 연산을 제거한다.
    for i in range(N - 1) :
        min_diff, max_gram = findClosestGroups(i)
        if min_diff < min_diff_so_far :
            min_diff_so_far = min_diff
            max_gram_so_far = max_gram
        elif min_diff == min_diff_so_far :
            max_gram_so_far = max(max_gram_so_far, max_gram)
    print(max_gram_so_far)
    
solve()