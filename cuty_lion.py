def solve() :
    N, K = tuple(map(int, input().split()))
    dolls = list(map(int, input().split()))
    l, r = 0, 0
    lion_cnt = 0
    min_length = -1
    while r < N :
        if dolls[r] == 1 : 
            lion_cnt += 1
        r += 1
        if r < N and lion_cnt == K :
            while l <= r and dolls[l] != 1:
                l += 1
            min_length = min(min_length, r - l) if min_length != -1 else r - l
            l += 1
            lion_cnt -= 1
            while l <= r and dolls[l] != 1 :
                l += 1

    if lion_cnt == K :
        while l < r and dolls[l] != 1:
                l += 1
        min_length = min(min_length, r - l) if min_length != -1 else r - l
    
    print(min_length)
    return

solve()