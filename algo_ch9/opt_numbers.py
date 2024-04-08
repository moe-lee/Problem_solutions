import sys

def solve() :
    N, M = list(map(int, sys.stdin.readline().split()))
    nums = []
    for _ in range(N) :
        nums.append(int(sys.stdin.readline()))
    min_dif = 2140000000
    nums.sort()
    l, r = 0, 1
    while(r < N) :
        pdif = nums[r] - nums[l]
        if(pdif < M) :
            r += 1
        else :
            min_dif = min(min_dif, pdif)
            if (l + 1 != r) : l += 1
            else : r += 1
    
    print(min_dif)
    return

if __name__ == '__main__' :
    solve()