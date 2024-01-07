def solve():
    n = int(input())
    a = list(map(lambda x : int(x), input().split()))
    s = sorted(a)
    res = [0] * n
    d = dict()
    for i in range(0, n) :
        oi = a.index(s[i])
        res[i] = oi
        a[oi] = -1

    for i in range(n) :
        d[res[i]] = i
    for i in range(n) :
        print(d[i], end=" ")
solve()