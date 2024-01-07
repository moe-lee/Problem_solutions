table = [0, 1, 2, 3, 5]

for i in range(5, 1001) :
    l, r = i // 2, (i//2 + 1) if i % 2 else (i // 2)
    table.append((table[l] * table[r] + table[l-1] * table[r-1]) % 15746)

def calcRes(n) :
    if n <= 1000 :
        return table[n]
    else :
        l, r = n // 2, (n//2 + 1) if n % 2 else (n // 2)
        return ((calcRes(l) * calcRes(r) % 15746) + (calcRes(l-1) * calcRes(r-1) % 15746)) % 15746


def solve() :
    n = int(input())
    print(calcRes(n))
solve()