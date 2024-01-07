def solve() :
    tbl = [0, 0]
    for i in range(2, 10 ** 6 + 1) :
        p = 9999999
        if(i % 3 == 0) :
            p = min(p, tbl[i // 3])
        if(i % 2 == 0) :
            p = min(p, tbl[i // 2])
        p = min(p, tbl[i-1])
        tbl.append(p + 1)

    x = int(input())
    print(tbl[x])

solve()