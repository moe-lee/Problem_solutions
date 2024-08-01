import sys
def solve() :
    n = int(sys.stdin.readline())
    ans = [-1] * n
    nums = list(map(int, sys.stdin.readline().split()))
    stack = []
    for idx, num in enumerate(nums) :
        while stack and stack[-1][1] < num :
            pev_idx, _ = stack.pop()
            ans[pev_idx] = num
        stack.append((idx, num))
    for n in ans :
        print(n, end=" ")

solve()