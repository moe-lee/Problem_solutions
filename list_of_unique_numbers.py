def solve() :
    N = int(input())
    nums = list(map(int, input().split()))
    combinations = 0
    l, r, o = 0, 0, 0
    dup_check = {}
    while r <= N :
        if r < N and nums[r] not in dup_check :
            dup_check[nums[r]] = 0
            r += 1
        else :
            combinations += int(((r+1-l) * (r - l)) / 2)
            if o > l :
                combinations -= int(((o + 1 - l) * (o - l)) / 2)
            if r == N : break
            dup_check.pop(nums[l])
            l += 1
            o = r
    print(combinations)
    return

if __name__ == '__main__' :
    solve()