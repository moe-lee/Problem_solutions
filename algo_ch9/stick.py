def solve() :
    x = int(input())
    cnt = 0
    while x > 0 :
        if x & 1 :
            cnt += 1
        x = x>>1
    print(cnt)
solve()