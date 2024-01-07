def solve() :
    N = int(input())
    n = N // 5
    m = N % 5
    p = 0
    while n >= 0 :
        if m % 3 == 0 :
            p = m // 3
            break
        else :
            n -= 1
            m += 5
    if(n < 0) : print(-1)
    else : print(n + p)

solve()