import sys
def solve() :
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    memo = [0] * 1001
    
    for num in nums :
        len = 0
        for i in range(num - 1, -1, -1) :
            len = max(len, memo[i])
        memo[num] = len + 1
    return max(memo)

print(solve())