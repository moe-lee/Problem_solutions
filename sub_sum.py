def solve():
    N, S = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    subsum = 0
    min_len = 1000000
    l, r = 0, 0
    while r != N or subsum >= S :
        if r < N and subsum < S :
            subsum += nums[r]
            r += 1
        else :
            min_len = min(min_len, r - l)
            subsum -= nums[l]
            l += 1
    if(subsum >= S) :
        min_len = min(min_len, r - l)
    
    if min_len == 1000000 : min_len = 0
    print(min_len)

if __name__ == "__main__" :
    solve()