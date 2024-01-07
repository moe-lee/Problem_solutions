table = [0, 1, 2, 4]
for i in range(4, 12) :
    table.append(table[i - 1] + table[i - 2] + table[i - 3])

def solve() :
    t = int(input())
    for i in range(t) :
        print(table[int(input())])


solve()