import sys

def solve() :
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    tab = [0] * 1001
    length = [[0,0] for _ in range(n)]
    for i in range(0, n) :
        j = nums[i] - 1
        max_precede = 0
        while j >= 0:
            max_precede = max(max_precede, tab[j])
            j -= 1
        tab[nums[i]] = max_precede + 1
        length[i][0] = tab[nums[i]]
    
    tab = [0] * 1001
    max_len = 0
    for i in range(n-1, -1, -1) :
        j = nums[i] - 1
        max_precede = 0
        while j >= 0:
            max_precede = max(max_precede, tab[j])
            j -= 1
        tab[nums[i]] = max_precede + 1
        length[i][1] = tab[nums[i]]
        max_len = max(max_len, length[i][0] + length[i][1])
    print(max_len - 1)
solve()