def solve():
    n = int(input())
    freinds = []
    for i in range(n) :
        freinds.append(list(input()))
    
    for i in range(0, n) :
        for j in range(0, n) :
            if freinds[i][j] == 'Y' :
                for k in range(0, n) :
                    if k != i and (freinds[i][k] != 'Y' and freinds[j][k] == 'Y') :
                        freinds[i][k] = 'K'
    max_freinds = 0
    for i in freinds :
        max_freinds = max(max_freinds, n - (i.count('N')))
    print(max_freinds)
solve()