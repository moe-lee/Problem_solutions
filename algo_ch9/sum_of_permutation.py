def solve() :
    n, l = tuple(map(lambda x : int(x), input().split()))
    o_sum = l * (l-1) / 2
    if (o_sum) > n :
        print(-1)
        return
    while l <= 100 :
        o_sum = 0
        i = int(((2*n / l) - l + 1) / 2)
        o_sum = l * (2 * i + l - 1) / 2
        if i < 0 :
            print(-1)
            return
        if o_sum == n :
            for i in range(i, i+l) :
                print(i, end=' ')
            return
        l += 1
    print(-1)
solve()