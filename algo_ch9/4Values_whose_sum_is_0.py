import sys

def solve() :
    lists = [[], [], [], []]
    n = int(sys.stdin.readline())
    negative_comb = ((0), (1), (2), (3),
                    (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
                    (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
    
    for _ in range(n) :
        values = list(map(int, sys.stdin.readline().split()))
        for i in range(4) :
            lists[i].append(values[i])
    for li in lists :
        li.sort()
    
    for comb in negative_comb :
        neg_indice = [0] * len(comb)
        if not all(map(lambda x: x < 0, [lists[comb[i]][0] for i in len(comb)])) :
            continue
        
    
    
solve()