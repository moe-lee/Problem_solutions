import bisect

def solve():
    l = int(input())
    s = sorted(list(map(lambda x : int(x), input().split())))
    n = int(input())
    
    i = bisect.bisect_left(s, n)
    if(s[i] == n) :
        print(0)
    else :
        a = n - (s[i - 1] if i > 0 else 0)
        b = s[i] - n
        print(a * b - 1)
solve()